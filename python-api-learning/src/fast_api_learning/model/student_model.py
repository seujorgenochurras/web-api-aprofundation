from typing import Optional
from pydantic.config import ConfigDict
from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.networks import EmailStr
from pydantic.v1.types import PyObject


class StudentModel(BaseModel):
    id: Optional[PyObject] = Field(alias="_id", default=None)
    name: str = Field(...)
    email: EmailStr = Field(...)
    course: str = Field(...)
    gpa: float = Field(..., le=4.0)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": 3.0,
            }
        },
    )