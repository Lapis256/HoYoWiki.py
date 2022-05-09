from __future__ import annotations

from typing import TypedDict, Union

from .filter import FiltersPayload
from .menu import MenusPayload


class Response(TypedDict):
    retcode: int
    message: str
    data: Union[FiltersPayload, MenusPayload]
