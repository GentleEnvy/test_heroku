from typing import Any, Final, final

from src.models import Subject
from src.urls.bases import IpSessionUrl


@final
class SubjectUrl(IpSessionUrl):
    """
    GET:
        Request:
            {
                `name`: <int>(
                    1 - mathematics
                    2 - russian language
                ) - name of the subject from the kim of EGE
            }
        Response:
            {
                `name`: <int> - name of the subject from the kim of EGE,
                `name`: <str> - subject name in Russian,
                `number_of_tasks`: <int> - number of tasks in 1 part  FIXME
            }
    """
    url: Final[str] = '/subject'

    def _get(self, request_json, session) -> dict[str, Any]:
        id_ = self.get_value(request_json, 'name')
        subject = Subject.get_by_id(id_)

        return subject.serialize()
