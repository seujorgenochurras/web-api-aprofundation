from typing import List
from fast_api_learning.model.student_model import StudentModel
from pydantic.main import BaseModel


class StudentCollection(BaseModel):
    students: List[StudentModel]