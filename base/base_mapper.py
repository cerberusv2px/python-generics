from abc import ABC, abstractmethod

from typing import Generic, TypeVar, List

E = TypeVar('E')
D = TypeVar('D')


class BaseMapper(ABC, Generic[E, D]):

    @abstractmethod
    def map_entity_to_dto(self, t: E) -> D:
        pass

    @abstractmethod
    def map_dto_to_entity(self, d: D) -> E:
        pass

    @abstractmethod
    def map_entities_to_dto(self, e: List[E]) -> List[D]:
        pass

    @abstractmethod
    def map_dtos_to_entities(self, d: List[D]) -> List[E]:
        pass
