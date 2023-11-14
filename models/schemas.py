from pydantic import BaseModel, EmailStr
from typing import List, Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    # class Config:
    #     from_attributes = True
    #     # orm_mode = True # изменили в pydantic v2


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


UserAuth = UserCreate


class LiteUser(UserBase):
    id: int


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    # class Config:
    #     from_attributes = True
    #     # orm_mode = True # изменили в pydantic v2


class Token(BaseModel):
    access_token: str
