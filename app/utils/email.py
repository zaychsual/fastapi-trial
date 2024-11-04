from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from .core.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM = settings.MAIL_FROM,
    MAIL_PORT = settings.MAIL_PORT,
    MAIL_SERVER = settings.MAIL_SERVER,
    MAIL_FROM_NAME = settings.MAIL_FROM_NAME,
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True
)

async def send_verification_email(email_to: str, username: str, token: str):
    message = MessageSchema(
        subject="Verify your email",
        recipients=[email_to],
        body=f"Hello {username}, use this token to verify your email: {token}"
    )
    fm = FastMail(conf)
    await fm.send_message(message)