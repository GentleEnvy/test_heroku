from typing import Any, final

from playhouse.postgres_ext import JSONField

from src.models.tasks.base_task import BaseTask

__all__ = ['MapTask']


@final
class MapTask(BaseTask):
    map: dict[str, Any] = JSONField()
