from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types.filter import FilterPayload


def parse_filters(filters: list[FilterPayload]):
    def func():
        for _filter in filters:
            yield Filter(
                _filter["key"],
                _filter["text"],
                list(map(FilterValue.from_json, _filter["values"])),
            )

    return list(func())


@dataclass
class FilterValue:
    id: str
    value: str

    @classmethod
    def from_json(cls, data):
        return cls(**data)


@dataclass
class Filter:
    key: str
    text: str
    values: list[FilterValue]
