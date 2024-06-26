from pydantic import BaseModel


class SUserAdd(BaseModel):
    login: str
    password: str

class SUser(SUserAdd): # S озачает что это schema
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


class SUserId(BaseModel):
    ok: bool = True
    user_id: int
