from datetime import date

today = date.today()
current_year = today.year

new_year = date(current_year + 1, 1 ,1)
weeks_until_new_year = (new_year - today).days // 7
print(f"weeks before new year: {weeks_until_new_year}")