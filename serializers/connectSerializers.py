from serializers.userSerializers import embeddedUserResponse
from bson.objectid import ObjectId


def connectEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "user_id": post["user_id"],
        "owner": post["owner"],
        "propertyType": post["propertyType"],
        "propertySize": post["propertySize"],
        "propertyPrice": post["propertyPrice"],
        "acccepted":post["acccepted"],
        "property": post["property"],
        "created_at": post["created_at"],
        "updated_at": post["updated_at"],
    }


def populatedconnectEntityEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "user_id": embeddedUserResponse(post["user"]),
        "owner": post["lname"],
        "propertyType": post["propertyType"],
        "propertySize": post["propertySize"],
        "propertyPrice": post["propertyPrice"],
        "acccepted":post["acccepted"],
        "property": post["property"],
        "created_at": post["created_at"],
        "updated_at": post["updated_at"],


    }
