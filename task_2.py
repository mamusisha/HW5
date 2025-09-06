from datetime import datetime, timedelta

today = datetime.today()
tuesday_index = 1
today_index = today.weekday()

days_until_next_tuesday = (7 - today_index + tuesday_index) % 7
if days_until_next_tuesday == 0:
    days_until_next_tuesday = 7

next_tuesday = today + timedelta(days=days_until_next_tuesday)
print("next tuesday:", next_tuesday.strftime("%Y-%m-%d"))