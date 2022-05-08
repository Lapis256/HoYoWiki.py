from __future__ import annotations
from typing import TYPE_CHECKING, Iterator

from .language import Language

if TYPE_CHECKING:
    from .http import HTTPClient
    from .types.entry_page import EntryPage as _EntryPage


def parse_entry_pages(
    http: HTTPClient, entry_pages: list[_EntryPage]
) -> list[EntryPage]:
    def func() -> Iterator[EntryPage]:
        for entry_page in entry_pages:
            yield EntryPage(http, **entry_page)

    return list(func())


class EntryPage:
    def __init__(
        self,
        http: HTTPClient,
        display_field: dict,
        entry_page_id: str,
        filter_values: dict,
        icon_url: str,
        name: str,
    ) -> None:
        self.http = http
        self.display_field = display_field
        self.entry_page_id = entry_page_id
        self.filter_values = filter_values
        self.icon_url = icon_url
        self.name = name

    def __repr__(self) -> str:
        return "<EntryPage entry_page_id={0.entry_page_id}, name={0.name}>".format(self)

    async def get_page(self, *, language: Language | None = None):
        data = await self.http.get_entry_page(self.entry_page_id, language=language)
        return data
