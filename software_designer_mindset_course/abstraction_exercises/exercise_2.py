from smtplib import SMTP
from typing import Protocol

DEFAULT_EMAIL = "support@arjancodes.com"
LOGIN = "test"
PASSWORD = "my_password"
HOST = "smtp.arjancodes.com"
PORT = 19584


class AbstractSMTP(Protocol):

    def connect(self, host: str, port: int):
        ...

    def login(self, username: str, password: str):
        ...

    def sendmail(self, from_address: str, to_address: str, message: str):
        ...

    def quit(self):
        ...

def send_email(
    server: AbstractSMTP, message: str, to_address: str, from_address: str = DEFAULT_EMAIL
) -> None:
    server.connect(HOST, PORT)
    server.login(LOGIN, PASSWORD)
    server.sendmail(from_address, to_address, message)
    server.quit()
