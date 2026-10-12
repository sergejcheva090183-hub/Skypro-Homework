from address import Address
from mailing import Mailing

address_from = Address(
    "109001", 
    "Волгоград", 
    "ул. Таганская", 
    "1", 
    "15"
)
address_to = Address(
    "197376", 
    "Рязань", 
    "ул. Профессора Попова", 
    "5", 
    "42"
)

my_mailing = Mailing(
    to_address=address_to,
    from_address=address_from,
    cost=450.50,
    track="RU123456789US"
)

print(
    f"Отправление {my_mailing.track} "
    f"из {my_mailing.from_address.index}, {my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, {my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} "
    
    f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. "
    
    f"Стоимость {my_mailing.cost} рублей."
)