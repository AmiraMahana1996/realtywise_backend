from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from schemas import  PropertyBaseSchema,CreatePropertySchema,UpdatePropertySchema
from database import Property
from oauth2 import require_user
from serializers.propertySerializers import propertyEntity, propertyListEntity
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

router = APIRouter()


# [...] Get All Posts
@router.get('/')
def get_posts(limit: int = 50, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    pipeline = [
        {'$match': {}},
        {'$lookup': {'from': 'users', 'localField': 'user',
                     'foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
        {
            '$skip': skip
        }, {
            '$limit': limit
        }
    ]
    properties = propertyListEntity(Property.aggregate(pipeline))
    return {'status': 'success', 'results': len(properties), 'properties': properties}

# [...] Create Post
@router.post('/', status_code=status.HTTP_201_CREATED)
def create_post(property: CreatePropertySchema):
    print(str(property.user))
    property.user = ObjectId(str(property.user))
    property.created_at = datetime.utcnow()
    property.updated_at = property.created_at
    try:
        result = Property.insert_one(property.dict())
        pipeline = [
            {'$match': {'_id': result.inserted_id}},
            {'$lookup': {'from': 'users', 'localField': 'user',
                         'foreignField': '_id', 'as': 'user'}},
            {'$unwind': '$user'},
        ]
        new_post = propertyListEntity(Property.aggregate(pipeline))[0]
        return new_post
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Post with title: '{property}' already exists")
    

# [...] Update Post
@router.put('/{id}')
def update_property(id: str, payload: UpdatePropertySchema, user_id: str = Depends(require_user)):
    print("amira")
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    updated_property = Property.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_property:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No post with this id: {id} found')
    return propertyEntity(updated_property)

 
# [...] Get Single Post
@router.get('/{id}')
def get_property(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    pipeline = [
        {'$match': {'_id': ObjectId(id)}},
        {'$lookup': {'from': 'users', 'localField': 'user',
                     'foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
    ]
    db_cursor = Property.aggregate(pipeline)
    results = list(db_cursor)

    if len(results) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No post with this id: {id} found")

    post = propertyListEntity(results)[0]
    return post

# [...] Delete Post
@router.delete('/{id}')
def delete_property(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    property = Property.find_one_and_delete({'_id': ObjectId(id)})
    if not property:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No post with this id: {id} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
