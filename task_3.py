import calendar

while True:
    year = input("enter year: ")
    if year.isdigit():
        break
    else:
        print("please enter a valid year")

if calendar.isleap(int(year)):
    print(f"year is leap: {year}")
else:
    print(f"year is not leap: {year}")