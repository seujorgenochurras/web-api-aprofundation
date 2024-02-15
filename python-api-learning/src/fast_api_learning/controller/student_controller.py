from src.fast_api_learning.model.student_model import StudentModel
from fastapi import APIRouter, Body, HTTPException
from bson.objectid import ObjectId
from src.fast_api_learning.main import student_collection

router = APIRouter()


@router.get(
"/student/{id}",
response_description="Get student by id",
response_model=StudentModel,
response_model_by_alias=False   
)
async def get_student_by_id(id: str):
    if( 
       student := await student_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return student
    raise HTTPException(status_code=404, detail=f"Student: {id} not found")

@router.post(
    "/student",
    response_description="Creates an student",
    response_model=StudentModel,
    response_model_by_alias=False
)
async def creat_student(student : StudentModel = Body(...)):
    """ Insert a new StudentModel 

    """
    
    new_student = await student_collection.insert_one(
    student.model_dump(by_alias=True, exclude=["id"]) # type: ignore
    )
    created_student = await student_collection.find_one(
        {"_id": new_student.inserted_id}
    )
    return created_student