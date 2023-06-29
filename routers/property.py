from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from schemas import  PostBaseSchema,PostBaseSchema
from database import Property
from oauth2 import require_user
from serializers.propertySerializers import propertyEntity, postListEntity
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError

router = APIRouter()


# @router.get('/')
# def get_properties(limit: int = 10, page: int = 1, search: str = '', user_id: str = Depends(require_user)):
#     skip = (page - 1) * limit
#     pipeline = [
#         {'$match': {}},
#         {'$lookup': {'from': 'users', 'localField': 'user',
#                      'foreignField': '_id', 'as': 'user'}},
#         {'$unwind': '$user'},
#         {
#             '$skip': skip
#         }, {
#             '$limit': limit
#         }
#     ]
#     posts = postListEntity(Post.aggregate(pipeline))
#     return {'status': 'success', 'results': len(posts), 'posts': posts}

@router.post('/create-property')
def create_post(property: PostBaseSchema):
    print(property)
    print('user_id')
    try:
        # result = Post.insert_one(post.dict())
        # pipeline = [
        #     {'$match': {'_id': result.inserted_id}},
        #     {'$lookup': {'from': 'users', 'localField': 'user',
        #                  'foreignField': '_id', 'as': 'user'}},
        #     {'$unwind': '$user'},
        # ]
        # print("tessst")
        # new_post = postListEntity(Post.aggregate(pipeline))[0]
        result = Property.insert_one(property.dict())
        return 'new_post'
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Post with title: '{property.property_code}' already exists")


@router.put('/update_property/{id}')
def update_post(id: str, payload: PostBaseSchema):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    updated_prpperty = Property.find_one_and_update(
        {'_id': ObjectId(id)}, {'$set': payload.dict(exclude_none=True)}, return_document=ReturnDocument.AFTER)
    if not updated_prpperty:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No post with this id: {id} found')
    return propertyEntity(updated_prpperty)


@router.get('/get_property/{id}')
def get_post(id: str):
    print(id)
    
    query = {"_id": ObjectId(id)}
 
    filter = {"_id": 0}
    res = Property.find_one(query, filter)
    print(res)
   
    return {"data":res,'statsu':"ok"}


@router.delete('/delete/{id}')
def delete_post(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    post = Property.find_one_and_delete({'_id': ObjectId(id)})
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No post with this id: {id} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)

