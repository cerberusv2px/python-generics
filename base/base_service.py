from abc import ABC

from typing import Generic, TypeVar

T = TypeVar('T')


class BaseService(ABC, Generic[T]):
    pass
