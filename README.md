# Email Marketing Tool

This is a simple Email Marketing Tool built using FastAPI and MongoDB.

## Features

- Send bulk emails via API
- Store email logs in MongoDB
- Input recipients via Swagger UI or CSV (future feature)

## How to Run

1. Clone the repo or download the code
2. Install required Python packages (see requirements.txt)
3. Set your MongoDB URI in `.env` file
4. Run the FastAPI app with:
   
   ```bash
   uvicorn main:app --reload

Access the API docs at http://localhost:8000/docs to send emails
