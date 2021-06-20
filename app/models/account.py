from pydantic import BaseModel, EmailStr


class AccountIn(BaseModel):
    name: str
    email: EmailStr
    password: str

class AccountPatch(BaseModel):
    name: str
    password: str

class Account(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
