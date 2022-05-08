from __future__ import annotations
from typing import TypedDict


class FilterValue(TypedDict):
    values: list[str]


class CharacterFilterValues(TypedDict, total=False):
    character_weapon: FilterValue
    character_property: FilterValue
    character_rarity: FilterValue
    character_region: FilterValue | None
    character_vision: FilterValue


class WeaponFilterValues(TypedDict):
    weapon_rarity: FilterValue
    weapon_type: FilterValue
    weapon_property: FilterValue


class ReliquaryFilterValues(TypedDict):
    reliquary_effect: FilterValue


class ReliquaryDisplayField(TypedDict):
    single_set_effect: str
    two_set_effect: str
    four_set_effect: str
    circlet_of_logos_icon_url: str
    sands_of_eon_icon_url: str
    plume_of_death_icon_url: str
    goblet_of_eonothem_icon_url: str
    flower_of_life_icon_url: str


class EnemyDisplayField(TypedDict):
    drop_materials: str


class EntryPage(TypedDict, total=False):
    filter_values: CharacterFilterValues | WeaponFilterValues | ReliquaryFilterValues
    icon_url: str
    name: str
    display_field: ReliquaryDisplayField | EnemyDisplayField | None
    entry_page_id: str | None
    id: str | None
    desc: str | None
    header_img_url: str | None
    modules: list[Module] | None
    menu_id: str | None
    menu_name: str | None


class Component(TypedDict):
    component_id: str
    layout: str
    data: str
    style: str


class Module(TypedDict):
    name: str
    has_edit_permission: bool
    is_poped: bool
    components: list[Component]


class EntryPageListPayload(TypedDict):
    list: list[EntryPage]
    total: str


class EntryPagePayload(TypedDict):
    page: EntryPage


class EntryPagesPayload(TypedDict):
    entry_pages: list[EntryPage]
