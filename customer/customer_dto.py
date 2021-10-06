from base.base_dto import BaseDto


class CustomerDto(BaseDto[int]):
    age: int
    name: str
