from __future__ import annotations
from typing import TYPE_CHECKING, Iterator

from .filter import parse_filters, FilterValue
from .entry_page import parse_entry_pages, EntryPage
from .language import Language
from .errors import PageNotExist

if TYPE_CHECKING:
    from .http import HTTPClient
    from .types.menu import Menu as _Menu
    from .types.entry_page import EntryPageListPayload


def parse_menus(http: HTTPClient, menus: list[_Menu]) -> list[Menu]:
    def func() -> Iterator[Menu]:
        for menu in menus:
            sub_menus: _Menu = menu.pop("sub_menus")
            yield Menu(http, **menu)
            yield from parse_menus(http, sub_menus)

    return list(func())


class Menu:
    def __init__(
        self, http: HTTPClient, id: str, name: str, style: str, has_page: bool
    ) -> None:
        self.http = http
        self.id = id
        self.name = name
        self.style = style
        self.has_page = has_page

    def __repr__(self) -> str:
        return "<Menu id={0.id}, name={0.name}>".format(self)

    async def get_filters(self, *, language: Language | None = None):
        if not self.has_page:
            raise PageNotExist

        data = await self.http.get_menu_filters(self.id, language=language)
        return parse_filters(data["filters"])

    async def get_entry_page_list(
        self,
        *,
        filters: list[FilterValue] | None = None,
        page_num: int = 1,
        page_size: int = 1,
        use_es: bool = True,
        language: Language | None = None,
    ) -> list[EntryPage]:
        if not self.has_page:
            raise PageNotExist
        if filters is None:
            filters = []

        data: EntryPageListPayload = await self.http.get_entry_page_list(
            self.id,
            filters=list(map(lambda f: f.id, filters)),
            page_num=page_num,
            page_size=page_size,
            use_es=use_es,
            language=language,
        )
        return parse_entry_pages(self.http, data["list"])

    async def get_entry_page_total(self, filters: list[FilterValue] | None = None):
        if not self.has_page:
            raise PageNotExist
        if filters is None:
            filters = []

        data: EntryPageListPayload = await self.http.get_entry_page_list(
            self.id,
            filters=list(map(lambda f: f.id, filters)),
            page_num=0,
            page_size=0,
            use_es=True,
            language=Language.en_us,
        )
        return int(data["total"])
