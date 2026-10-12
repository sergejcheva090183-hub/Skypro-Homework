from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15 Pro", "+79161234567"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79267654321"),
    Smartphone("Xiaomi", "14 Pro", "+79031112233"),
    Smartphone("Google", "Pixel 8", "+79250001122"),
    Smartphone("Huawei", "Mate 60 Pro", "+79859998877")
]

for phone  in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")