from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from email_utils import send_email
from models import log_email_result

app = FastAPI()

class EmailRequest(BaseModel):
    emails: List[str]

@app.post("/send-emails")
def send_bulk_emails(request: EmailRequest):
    subject = "Mail from Priyanshu!"
    body = "Hi there,\n\nThanks for providing your email for testing Its working now .\n\nThanks\n- Priyanshu Gairola"

    results = []

    for email in request.emails:
        success = send_email(email, subject, body)
        log_email_result(email, success)

        results.append({
            "email": email,
            "status": "sent" if success else "failed"
        })

    return {
        "results": results
    }
