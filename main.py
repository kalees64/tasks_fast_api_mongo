from fastapi import FastAPI
from src.task.task_controller import task_controller
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="VK64 Tasks API",
    version="0.0.1"
)

@app.get("/")
def vk64():
    return {"data": "VK64 Tasks API"}


app.include_router(task_controller)

origins = ["http://localhost:4200","http://localhost:5173","http://localhost:5000"]
app.add_middleware(
                   CORSMiddleware,
                   allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"]
                   )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)