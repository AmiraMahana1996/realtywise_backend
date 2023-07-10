from serializers.userSerializers import embeddedUserResponse


def propertyEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "fname": post["fname"],
        "lname": post["lname"],
        "contactNumber": post["contactNumber"],
        "phoneNumber": post["phoneNumber"],
        "emial": post["emial"],
        "DOB":post["DOB"],
        "city": post["city"],
        "coudescntry": post["desc"],
        "zip_code": post["zip_code"],
        "desc": post["desc"],
        "propertyType": post["propertyType"],
        "propertySize": post["propertySize"],
        "price": post["price"],
        "propertyAddressLine1": post["propertyAddressLine1"],
        "propertyAddressLine2": post["propertyAddressLine2"],
        "propertyAddressLine3": post["propertyAddressLine3"],
        "images": post["images"],
        "advertising": post["advertising"],
    }


def populatedPropertyEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "fname": post["fname"],
        "lname": post["lname"],
        "contactNumber": post["contactNumber"],
        "phoneNumber": post["phoneNumber"],
        "emial": post["emial"],
        "DOB":post["DOB"],
        "city": post["city"],
        "coudescntry": post["desc"],
        "zip_code": post["zip_code"],
        "desc": post["desc"],
        "propertyType": post["propertyType"],
        "propertySize": post["propertySize"],
        "price": post["price"],
        "propertyAddressLine1": post["propertyAddressLine1"],
        "propertyAddressLine2": post["propertyAddressLine2"],
        "propertyAddressLine3": post["propertyAddressLine3"],
        "images": post["images"],
        "advertising": post["advertising"],
        "user": embeddedUserResponse(post["user"]),
        "created_at": post["created_at"],
        "updated_at": post["updated_at"],
    }


def propertyListEntity(posts) -> list:
    return [populatedPropertyEntity(post) for post in posts]

