from pymongo import MongoClient

# mongo_db_url = "mongodb://localhost:27017/"
mongo_db_url = "mongodb+srv://kalees64:vairamages64@vk64.ocujln3.mongodb.net/vk64-task-app?retryWrites=true&w=majority&appName=VK64"
database_name="vk64-task-app"
tasks_collection_name="tasks"

mongo_client = MongoClient(mongo_db_url)
db = mongo_client[database_name]
tasks_collection = db[tasks_collection_name]