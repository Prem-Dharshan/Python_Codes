import datetime
year = int(input("Enter the year (e.g. 2013): "))
month = int(input("Enter the month (e.g. 11): "))
day = int(input("Enter the day (e.g. 18): "))
date = datetime.date(year, month, day)

successor = date + datetime.timedelta(days=1)

print("The day immediately after", date, "is", successor)
