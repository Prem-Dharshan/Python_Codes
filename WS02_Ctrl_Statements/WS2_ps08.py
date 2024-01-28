# code 8
price_per_loaf = 75.00
discount_percent = 60

loaves = int(input("Enter the number of loaves: "))
day_old = input("Is the bread day old? (y/n)")

regular_price = loaves * price_per_loaf

if day_old.lower() == "y":
    discount = regular_price * (discount_percent / 100)
    total_price = regular_price - discount
else:
    discount = 0
    total_price = regular_price

print(f"Regular price: Rs. {regular_price:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Total price: Rs. {total_price:.2f}")
