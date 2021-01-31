from logging import exception
from typing import Final
from smtplib import SMTP
from email.message import EmailMessage
import ssl

from src.utils.interfaces import Email

__all__ = ['SmtpEmail']


class SmtpEmail(Email):
    """
    Util class for sending emails, TODO: more email functional
    """

    def __init__(self, login: str, password: str):
        """
        :param login: login of the account from which the emails will be sent
        :param password: password of the account from which the emails will be sent
        """
        self._login: Final[str] = login
        self._smtp: Final[SMTP] = SMTP('smtp.gmail.com', 587)
        self._smtp.ehlo()
        self._smtp.starttls(context=ssl.create_default_context())
        self._smtp.login(login, password)

    def send(self, message, to, subject=None) -> None:
        try:
            email_message = EmailMessage()

            email_message.set_content(message)
            email_message['From'] = self._login
            email_message['To'] = to
            if subject:
                email_message['Subject'] = subject

            self._smtp.send_message(email_message)
        except:  # FIXME: check raises
            exception(f'{message = },\n{to = },\n{subject = }')
