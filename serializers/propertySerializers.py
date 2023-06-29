
def propertyEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "owner_name": post["owner_name"],
        "owner_phone": post["owner_phone"],
        "owner_address_line1": post["owner_address_line1"],
        "owner_address_line2": post["owner_address_line2"],
        "owner_address_line3": post["owner_address_line3"],
        "email":post["email"],
        "city": post["city"],
        "country": post["country"],
        "zip_code": post["zip_code"],
        "description": post["description"],
        "property_type": post["property_type"],
        "property_name": post["property_name"],
        "property_size": post["property_size"],
        "property_accepted_price_range": post["property_accepted_price_range"],
        "property_address_line1": post["property_address_line1"],
        "property_address_line2": post["property_address_line2"],
        "property_zipCode": post["property_zipCode"],
        "property_images": post["property_images"],
        "property_code": post["property_code"],
        "property_code": post["property_code"],
        "created_at": post["created_at"],
        "updated_at": post["updated_at"],
        "created_by": post["created_by"]
    }


def populatedPostEntity(post) -> dict:
    return {
        "id": str(post["_id"]),
        "owner_name": post["owner_name"],
        "owner_phone": post["owner_phone"],
        "owner_address_line1": post["owner_address_line1"],
        "owner_address_line2": post["owner_address_line2"],
        "owner_address_line3": post["owner_address_line3"],
        "email":post["email"],
        "city": post["city"],
        "country": post["country"],
        "zip_code": post["zip_code"],
        "description": post["description"],
        "property_type": post["property_type"],
        "property_name": post["property_name"],
        "property_size": post["property_size"],
        "property_accepted_price_range": post["property_accepted_price_range"],
        "property_address_line1": post["property_address_line1"],
        "property_address_line2": post["property_address_line2"],
        "property_zipCode": post["property_zipCode"],
        "property_images": post["property_images"],
        "property_code": post["property_code"],
        "property_code": post["property_code"],
        "created_at": post["created_at"],
        "updated_at": post["updated_at"],
        "created_by": post["created_by"]
    }


def postListEntity(posts) -> list:
    return [populatedPostEntity(post) for post in posts]

