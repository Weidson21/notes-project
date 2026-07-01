from pydantic import BaseModel, Field
from datetime import datetime, UTC, timezone


class NoteIn(BaseModel):
    title: str = Field(min_length=8, max_length=20)
    anotation: str = Field(min_length=3, max_length=500, default="No anotation")

class NoteOut(BaseModel):
    id: int
    title: str
    anotation: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class NoteUpdate(BaseModel):
    title: str | None = None
    anotation: str | None = None
