from __future__ import annotations
from aiohttp import ClientSession
from typing import TYPE_CHECKING

from .errors import PageNotExist

if TYPE_CHECKING:
    from .language import Language
    from .types.http import Responce
    from .types.menu import MenusPayload
    from .types.filter import FiltersPayload
    from .types.entry_page import (
        EntryPageListPayload,
        EntryPagePayload,
        EntryPagesPayload,
    )


class HTTPClient:
    BASE = "https://sg-wiki-api-static.hoyolab.com/hoyowiki/wapi/"

    def __init__(self, default_language: Language) -> None:
        self.__session = ClientSession()
        self.default_language: Language = default_language

    async def request(
        self,
        method: str,
        path: str,
        language: Language | None = None,
        params=None,
        payload=None,
    ):
        kwargs = {
            "headers": {"x-rpc-language": (language or self.default_language).value},
        }
        if params is not None:
            kwargs["params"] = params
        if payload is not None:
            kwargs["json"] = payload

        async with self.__session.request(method, self.BASE + path, **kwargs) as res:
            if res.status != 200:
                raise

            data: Responce = await res.json()
            if data["retcode"] in [404, -1]:
                raise PageNotExist

            return data["data"]

    async def close(self):
        await self.__session.close()

    async def get_menus(self, language: Language | None) -> MenusPayload:
        data = await self.request("GET", "get_menus", language=language)
        return data

    async def get_menu_filters(
        self, id: str, *, language: Language | None
    ) -> FiltersPayload:
        data = await self.request(
            "GET", "get_menu_filters", language=language, params={"menu_id": id}
        )
        return data

    def get_entry_page_list(
        self,
        id: str,
        *,
        filters: list[str],
        page_num: int,
        page_size: int,
        use_es: bool,
        language: Language | None,
    ) -> EntryPageListPayload:
        return self.request(
            "POST",
            "get_entry_page_list",
            language=language,
            payload={
                "menu_id": id,
                "filters": filters,
                "page_num": page_num,
                "page_size": page_size,
                "use_es": use_es,
            },
        )

    def get_entry_page(self, id: str, *, language: Language | None) -> EntryPagePayload:
        return self.request(
            "GET", "entry_page", language=language, params={"entry_page_id": id}
        )

    def get_entry_pages(
        self, ids: list[str], *, language: Language | None
    ) -> EntryPagesPayload:
        return self.request(
            "POST", "entry_pages", language=language, payload={"entry_page_ids": ids}
        )
