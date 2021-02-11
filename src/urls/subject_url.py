from typing import Any, Final, final

from src.models import Subject
from src.urls.bases import IpSessionUrl


@final
class SubjectUrl(IpSessionUrl):
    """
    GET:
        Request:
            {
                `id`: <int>(
                    1 - russian language
                    2 - mathematics
                ) - id of the subject from the kim of EGE
            }
        Response:
            {
                `id`: <int> - id of the subject from the kim of EGE,
                `name`: <str> - subject name in Russian
            }
    """
    url: Final[str] = '/subject'

    def _get(self, request_json, session) -> dict[str, Any]:
        id_ = self.get_value(request_json, 'name')
        subject = Subject.get_by_id(id_)

        return subject.serialize()
