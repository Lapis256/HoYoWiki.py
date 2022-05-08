from __future__ import annotations
from typing import TYPE_CHECKING

from .http import HTTPClient
from .menu import parse_menus

if TYPE_CHECKING:
    from .types.menu import MenusPayload
    from .language import Language


class API:
    def __init__(self, default_language: Language):
        self.http = HTTPClient(default_language)

    async def close(self):
        await self.http.close()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *_):
        await self.close()

    async def get_menus(self, *, language: Language | None = None):
        data: MenusPayload = await self.http.get_menus(language)
        return parse_menus(self.http, data["menus"])

    async def get_page(self, id: str, *, language: Language | None = None):
        data = await self.http.get_entry_page(id, language=language)
        return data

    async def get_pages(self, ids: list[str], *, language: Language | None = None):
        data = await self.http.get_entry_pages(ids, language=language)
        return data
