from customer.customer_dto import CustomerDto
from customer.customer_mapper import CustomerMapper


def main():
    customer_dto = CustomerDto(id=1, name='customer1', age=33)
    print(type(customer_dto))

    mapper = CustomerMapper()
    print(type(mapper.map_dto_to_entity(customer_dto)))


if __name__ == '__main__':
    main()
