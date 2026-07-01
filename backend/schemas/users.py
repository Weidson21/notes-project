from pydantic import BaseModel, Field

class UserIn(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = Field(regex=r'^\S+@\S+\.\S+$')
    password: str = Field(min_length=6, max_length=12)

class UserOut(BaseModel):
    id: int
    username: str
    email: str

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None