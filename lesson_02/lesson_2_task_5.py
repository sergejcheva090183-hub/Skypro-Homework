def month_to_season(month):
    
    if not isinstance(month, int) or month < 1 or month > 12:
        return "Ошибка: введите число от 1 до 12"
    if month == 12 or month == 1 or month == 2:
        return "Зима"
    elif month == 3 or month == 4 or month == 5:
        return "Весна"
    elif month == 6 or month == 7 or month == 8:
        return "Лето"
    else:
        return "Осень"

user_month = int(input("Введите порядковый номер месяца (от 1 до 12): "))
    
season_name = month_to_season(user_month) 
print(f"Месяц {user_month} — это {season_name}")