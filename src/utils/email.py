from typing import Final
from smtplib import SMTP
from email.message import EmailMessage

__all__ = ['Email']


class Email:
    def __init__(self, login: str, password: str):
        self._login: Final[str] = login
        self._smtp: Final[SMTP] = SMTP('smtp.gmail.com', 587)
        self._smtp.starttls()
        self._smtp.login(login, password)

    def send(self, message: str, to: str, subject: str = None) -> None:
        """
        :param message: the text of the e-mail
        :param to: to whom the e-mail is sent
        :param subject: the subject of the e-mail
        :raises TODO
        """
        email_message = EmailMessage()

        email_message.set_content(message)
        email_message['From'] = self._login
        email_message['To'] = to
        if subject:
            email_message['Subject'] = subject

        self._smtp.send_message(email_message)
