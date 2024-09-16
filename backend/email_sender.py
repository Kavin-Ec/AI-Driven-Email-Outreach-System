import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EmailDetails(BaseModel):
    recipient_email: str
    subject: str
    body: str

@router.post("/send")
async def send_email(ed: EmailDetails):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "eckavin2002@gmail.com"
    password = "eudgfkapxisczads"  # Use app password, not Gmail account password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ed.recipient_email
    msg['Subject'] = ed.subject
    msg.attach(MIMEText(ed.body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        return {"status": "Email sent"}
    except Exception as e:
        return {"error": str(e)}
