from fastapi import FastAPI
from src.task.task_controller import task_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="VK64 Tasks API",
    version="0.0.1"
)


app.include_router(task_controller)

origins = ["http://localhost:4200","http://localhost:5173","http://localhost:5000"]
app.add_middleware(
                   CORSMiddleware,
                   allow_origins = origins,
                   allow_credentials = True,
                   allow_methods = ["*"],
                   allow_headers = ["*"]
                   )