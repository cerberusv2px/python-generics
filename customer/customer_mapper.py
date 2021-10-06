from typing import List

from base.base_mapper import BaseMapper
from customer.customer_dto import CustomerDto
from customer.customer_entity import CustomerEntity


class CustomerMapper(BaseMapper[CustomerDto, CustomerEntity]):
    def map_entity_to_dto(self, t: CustomerEntity) -> CustomerDto:
        return CustomerDto(id=t.id, created_at=t.created_at, version=t.version, name=t.name, age=t.age)

    def map_dto_to_entity(self, d: CustomerDto) -> CustomerEntity:
        return CustomerEntity(id=d.id, created_at=d.created_at, version=d.version, name=d.name, age=d.age)

    def map_entities_to_dto(self, e: List[CustomerEntity]) -> List[CustomerDto]:
        return [self.map_entity_to_dto(entity) for entity in e]

    def map_dtos_to_entities(self, d: List[CustomerDto]) -> List[CustomerEntity]:
        return [self.map_dto_to_entity(dto) for dto in d]
