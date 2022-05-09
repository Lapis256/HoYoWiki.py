from __future__ import annotations

from typing import TypedDict


class FilterValue(TypedDict):
    id: str
    value: str


class FilterPayload(TypedDict):
    key: str
    text: str
    values: list[FilterValue]


class FiltersPayload(TypedDict):
    filters: list[FilterPayload]
