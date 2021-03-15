from typing import Any

from playhouse.postgres_ext import JSONField

from src.models.tasks.base_task import BaseTask

__all__ = ['MapTask']


class MapTask(BaseTask):
    map: dict[str, Any] = JSONField()
