from pymongo import MongoClient
import os
from dotenv import load_dotenv
from datetime import datetime

# Load .env variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["email_marketing"]
emails_collection = db["emails"]

def log_email_result(to_email: str, success: bool):
    emails_collection.insert_one({
        "email": to_email,
        "success": success,
        "timestamp": datetime.utcnow()
    })
