from typing import Generic, TypeVar

from base.custom_base_model import CustomBaseModel

T = TypeVar('T')


class BaseDto(Generic[T], CustomBaseModel):
    id: T
    created_at: str = '2021'
    version: float = 1.0
