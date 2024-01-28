# code 18
month = input("Enter a month : ")
if month.lower() in ["january", "march", "may", "july", "august", "october", "december"]:
  print("It has 31 days")
elif month.lower() == 'febrauary':
  print("It has 28 or 29 days.")
elif month.lower() in ['april', 'june', 'september', 'november']:
  print("It has 30 days")
else:
  print("Invald month!")
