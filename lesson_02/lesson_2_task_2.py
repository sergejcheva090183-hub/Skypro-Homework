def is_year_leap(year):
    return True if year % 4 == 0 else False

lyear = int(input("Введите год: "))

is_leap = is_year_leap(lyear)
print(f"год {lyear}: {is_leap}")