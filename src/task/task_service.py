from src.db.db import tasks_collection
from fastapi import HTTPException
from .task_model import *
from bson import ObjectId


def get_all_tasks():
    try:
        allTasks = tasks_collection.find()
        tasks = [reFactorTask(task) for task in allTasks]
        return {"data":tasks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
def get_task_by_id(task_id: str):
    try:
        task = tasks_collection.find_one({"_id": ObjectId(task_id)})
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"data": reFactorTask(task)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
def create_task(task:CreateTaskModel):
    try:
        new_task = tasks_collection.insert_one(task.model_dump(by_alias=True))
        task = get_task_by_id(new_task.inserted_id)
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
def update_task(task_id: str, updated_task: "UpdateTaskModel"):
    try:
        existing_task = tasks_collection.find_one({"_id": ObjectId(task_id)})

        if not existing_task:
            raise HTTPException(status_code=404, detail="Task not found")

        update_data = updated_task.model_dump(exclude_unset=True, by_alias=True)

        update_data.pop("_id", None)

        if "modifiedAt" not in update_data:
            update_data["modifiedAt"] = datetime.now()

        result = tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")

        return get_task_by_id(task_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
    
def delete_task(task_id: str):
    try:
        task = get_task_by_id(task_id)
        result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
def reFactorTask(task):
    return {
                    "_id": str(task["_id"]),
                    "title": task["title"],
                    "description": task["description"],
                    "status": task["status"],
                    "createdAt": task.get("createdAt"),   
                    "createdBy": task.get("createdBy"),   
                    "modifiedAt": task.get("modifiedAt"), 
                    "priority": task.get("priority"),
                    "dueDate": task.get("dueDate"),       
    }