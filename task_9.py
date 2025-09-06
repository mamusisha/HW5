from datetime import date

def to_birthday():
    print("enter your birthday:")
    year = int(input("year (e.g., 2000): "))
    month = int(input("month (1-12): "))
    day = int(input("day (1-31): "))
    birthday = date(year, month, day)
    today = date.today()

    next_birthday = date(today.year, birthday.month, birthday.day)
    if next_birthday <= today:
        next_birthday = date(today.year + 1, birthday.month, birthday.day)
    days_until_birthday = (next_birthday - today).days
    print(f"next birthday: {next_birthday}")
    print(f"days until your next birthday: {days_until_birthday}")

to_birthday()