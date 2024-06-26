from pydantic import BaseModel


class SUserAdd(BaseModel):
    login: str
    password: str

class SUser(SUserAdd): # S озачает что это schema
    id: int


class SUserId(BaseModel):
    ok: bool = True
    user_id: int
