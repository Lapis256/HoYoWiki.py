from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .types.filter import (
        Filter as FilterPayload,
        FilterValue as FilterValuePayload,
        Filters,
    )


def parse_filters(filters: Filters):
    def func():
        for filter in filters:
            values = filter.pop("values")
            yield Filter(
                **filter,
                values=list(map(FilterValue.from_json, values)),
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
