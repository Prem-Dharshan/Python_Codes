
seconds = int(input("Enter the number of seconds: "))

if seconds >= 86400:
    days = seconds // 86400
    print(f"{days} day(s)")
    seconds = seconds % 86400

if seconds >= 3600:
    hours = seconds // 3600
    print(f"{hours} hour(s)")
    seconds = seconds % 3600

if seconds >= 60:
    minutes = seconds // 60
    print(f"{minutes} minute(s)")
    seconds = seconds % 60

print(f"{seconds} second(s)")
