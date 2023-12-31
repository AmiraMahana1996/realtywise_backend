from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from typing import List
from bson.objectid import ObjectId


class UserBaseSchema(BaseModel):
    name: str
    email: str

    city: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


# user schema

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema


class FilteredUserResponse(UserBaseSchema):
    id: str

# end user schema


# property schema

class PropertyBaseSchema(BaseModel):
    fname: str
    lname: str
    contactNumber: str
    phoneNumber: str
    emial: str
    DOB: str
    city: str
    zip_code: str
    desc: str
    propertyType: str
    propertySize: str
    price: str
    propertyAddressLine1: str
    propertyAddressLine2: str
    propertyAddressLine3: str
    images: list
    advertising: str
    advertisingImageCover: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class CreatePropertySchema(PropertyBaseSchema):
    user: str
    pass


class PropertyResponse(PropertyBaseSchema):
    id: str
    advertisingImageCover: str
    user: FilteredUserResponse
    created_at: datetime
    updated_at: datetime


class UpdatePropertySchema(BaseModel):
    fname: str
    lname: str
    contactNumber: str
    phoneNumber: str
    emial: str
    DOB: str
    city: str
    zip_code: str
    desc: str
    propertyType: str
    propertySize: str
    price: str
    propertyAddressLine1: str
    propertyAddressLine2: str
    propertyAddressLine3: str
    images: list
    advertising: str
    advertisingImageCover: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ListPropertyResponse(BaseModel):
    status: str
    results: int
    posts: List[PropertyResponse]


class ConnectBaseSchema(BaseModel):
    user_id: str
    owner: str
    property: str
    propertyType: str
    propertySize: str
    propertyPrice: str
    acccepted: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
