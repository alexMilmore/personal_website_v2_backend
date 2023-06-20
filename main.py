from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import smtplib, ssl

app = FastAPI()

origins = [
    "https://alexmilmore.com",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

port = 465  # For SSL
password = "_dP$.gZn-xX8r,#"
context = ssl.create_default_context()

class ContactMessage(BaseModel):
    sender: str
    msg: str

@app.post("/contact")
async def editLine(message: ContactMessage):
    try:
        with smtplib.SMTP_SSL("mail.privateemail.com", port, context=context) as server:
            server.login("amilmore@alexmilmore.com", password)
            server.sendmail("amilmore@alexmilmore.com", "amilmore@alexmilmore.com", f"FROM\n{message.sender}\n\nMESSAGE\n{message.msg}")
        return {"success": True}
    except:
        return {"success": False}
