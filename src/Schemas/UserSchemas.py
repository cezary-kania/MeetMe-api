from pydantic import BaseModel

class UserBase(BaseModel):
    email: str


class UserNew(UserBase):
    password: str