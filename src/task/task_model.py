from pydantic import BaseModel,Field
from typing import Any,Optional
from datetime import datetime




class CreateTaskModel(BaseModel):
    title: str
    description: str
    status:bool
    created_at:Optional[datetime] = Field(default_factory=datetime.now,alias="createdAt")
    created_by:Optional[str] = Field(None,alias="createdBy")
    modified_by:Optional[str] = Field(None,alias="modifiedBy")
    modified_at:Optional[datetime] = Field(default_factory=datetime.now,alias="modifiedAt")
    priority: Optional[str] = Field(None, alias="priority") 
    due_date: Optional[datetime] = Field(None, alias="dueDate") 

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class UpdateTaskModel(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    priority: Optional[str] = Field(None, alias="priority") 
    due_date: Optional[datetime] = Field(None, alias="dueDate")
    modified_by:Optional[str] = Field(None,alias="modifiedBy")
    modified_at: Optional[datetime] = Field(default_factory=datetime.now,alias="modifiedAt")

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class ResponseModel(BaseModel):
    id:str = Field(alias="_id")
    title: str
    description: str
    status:bool
    created_at:Optional[datetime]  = Field(alias="createdAt")
    created_by:Optional[str] = Field(alias="createdBy")
    modified_at:Optional[datetime] = Field(alias="modifiedAt")
    priority: Optional[str] 
    due_date: Optional[datetime] = Field(alias="dueDate")



class ResponseModelForAllTasks(BaseModel):
    data:list[ResponseModel]

class ResponseModelForSingleTask(BaseModel):
    data:ResponseModel