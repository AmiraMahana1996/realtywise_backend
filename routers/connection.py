from bson import json_util
from datetime import datetime
from fastapi import Depends, HTTPException, status, APIRouter, Response
from pymongo.collection import ReturnDocument
from schemas import PropertyBaseSchema, CreatePropertySchema, ConnectBaseSchema
from database import Connect
from oauth2 import require_user
from serializers.propertySerializers import propertyEntity, propertyListEntity
from serializers.connectSerializers import populatedconnectEntityEntity

from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
import urllib.request
import json
router = APIRouter()


@router.post('/create-conect')
def create(connect: ConnectBaseSchema):
    print(connect)
    connect.created_at = datetime.utcnow()
    connect.updated_at = connect.created_at
    result = Connect.insert_one(connect.dict())
    pipeline = [
        {'$match': {'_id': result.inserted_id}},
        {'$lookup': {'from': 'users', 'localField': 'user',
                     'foreignField': '_id', 'as': 'user'}},
        {'$unwind': '$user'},
    ]
    new_connect = Connect.aggregate(pipeline)
    return json.loads(json_util.dumps({"result": "success"}))


@router.get('/{id}')
def get_connect(id: str):
    _id = str(id)
    print(_id)
    connect = Connect.find({"user_id": _id})
    return json.loads(json_util.dumps(connect))


@router.get('/details/{id}')
def get_connect(id: str):
    _id = ObjectId(str(id))
    print(_id)
    connect = Connect.find_one({"_id": _id})
    return json.loads(json_util.dumps(connect))


@router.get('/recieved/{id}')
def get_recieved_connect(id: str):
    Id = str(id)
    connections = Connect.find({"owner": Id, "acccepted": "False"})
    return json.loads(json_util.dumps(connections))


@router.get('/accepted/{id}')
def get_recieved_connect(id: str):
    Id = str(id)
    connections = Connect.find({"user_id": Id, "acccepted": "True"})
    return json.loads(json_util.dumps(connections))


@router.put('/do-accept/{id}')
def get_accept_connect(id: str):
    Id = str(id)
    connections = Connect.find_one_and_update(
        {'_id': ObjectId(Id)}, {'$set': {"acccepted": "True"}}, return_document=ReturnDocument.AFTER)
    return json.loads(json_util.dumps(connections))


@router.get('/get-connections/{userId}')
def get_posts(userId: str):
    print(userId)
    connections = Connect.find({"user_id": str(userId)})

    return {'status': 'success', 'results': 'success', 'connections': json.loads(json_util.dumps(connections))}


@router.delete('/{id}')
def delete_property(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Invalid id: {id}")
    connect = Connect.find_one_and_delete({'_id': ObjectId(id)})
    if not connect:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No post with this id: {id} found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)
