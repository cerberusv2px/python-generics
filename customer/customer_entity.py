from base.base_entity import BaseEntity


class CustomerEntity(BaseEntity[int]):
    age: int
    name: str
