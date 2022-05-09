from __future__ import annotations

from typing import TypedDict


class Menu(TypedDict):
    has_page: bool
    id: str
    name: str
    style: str
    sub_menus: list[Menu]


class MenusPayload(TypedDict):
    menus: list[Menu]
