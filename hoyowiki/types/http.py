from __future__ import annotations
from typing import TypedDict

from .filter import FiltersPayload
from .menu import MenusPayload


class Responce(TypedDict):
    retcode: int
    message: str
    data: FiltersPayload | MenusPayload
