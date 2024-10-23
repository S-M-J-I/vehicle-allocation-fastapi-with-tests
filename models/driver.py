from pydantic import BaseModel, Field
from models.py_obj import PyObjectId
from typing import Optional
from bson import ObjectId


class Driver(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
