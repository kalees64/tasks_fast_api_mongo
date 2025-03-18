from fastapi import APIRouter
from . import task_service
from starlette import status
from .task_model import *

task_controller = APIRouter(
    tags=["Tasks"],
    prefix="/tasks",
)

@task_controller.get("/",status_code=status.HTTP_200_OK,response_model=ResponseModelForAllTasks)
def get_all_tasks():
    return task_service.get_all_tasks()

@task_controller.get("/{task_id}", status_code=status.HTTP_200_OK, response_model=ResponseModelForSingleTask)
def get_task(task_id: str):
    return task_service.get_task_by_id(task_id)

@task_controller.post("/",status_code=status.HTTP_201_CREATED,response_model=ResponseModelForSingleTask)
def create_task(task:CreateTaskModel):
    return task_service.create_task(task)


@task_controller.patch("/{task_id}", status_code=status.HTTP_200_OK, response_model=ResponseModelForSingleTask)
def update_task_by_id(task_id: str, updated_task: UpdateTaskModel):
    return task_service.update_task(task_id, updated_task)

@task_controller.delete("/{task_id}", status_code=status.HTTP_200_OK,response_model=ResponseModelForSingleTask)
def delete_task_by_id(task_id: str):
    return task_service.delete_task(task_id)