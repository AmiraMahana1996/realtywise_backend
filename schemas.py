from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from typing import List
from bson.objectid import ObjectId

class UserBaseSchema(BaseModel):
    name: str
    email: str
  
    role: str | None = None
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


class PostBaseSchema(BaseModel):
    owner_name: str
    owner_phone: str
    owner_address_line1: str
    owner_address_line2: str
    owner_address_line3: str
    email: str
    city: str
    country: str
    zip_code: str
    description: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
    created_by: str
    property_type:str
    property_name:str
    property_size:str
    property_accepted_price_range:str
    property_address_line1:str
    property_address_line2:str
    property_zipCode:str
    property_images:str
    property_code:str
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


