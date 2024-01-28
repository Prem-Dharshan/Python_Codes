# code 17
# Constants for the base plan
BASE_MINUTES = 50
BASE_MESSAGES = 50
BASE_CHARGE = 15.00
ADDITIONAL_MINUTE_CHARGE = 0.25
ADDITIONAL_MESSAGE_CHARGE = 0.15
TAX_RATE = 0.05
NINE_ONE_ONE_FEE = 0.44

# Get input from user
minutes_used = int(input("Enter the number of minutes used: "))
messages_used = int(input("Enter the number of text messages used: "))

# Calculate the additional minutes and messages charges
additional_minutes = (minutes_used - BASE_MINUTES) * \
    ADDITIONAL_MINUTE_CHARGE if minutes_used > BASE_MINUTES else 0
additional_messages = (messages_used - BASE_MESSAGES) * \
    ADDITIONAL_MESSAGE_CHARGE if messages_used > BASE_MESSAGES else 0

# Calculate the subtotal
subtotal = BASE_CHARGE + additional_minutes + \
    additional_messages + NINE_ONE_ONE_FEE

# Calculate the tax
tax = subtotal * TAX_RATE

# Calculate the total bill
total_bill = subtotal + tax

# Display the bill
print("Base Charge: $%.2f" % BASE_CHARGE)
if additional_minutes > 0:
    print("Additional minutes charge: $%.2f" % additional_minutes)
if additional_messages > 0:
    print("Additional messages charge: $%.2f" % additional_messages)
print("911 Fee: $%.2f" % NINE_ONE_ONE_FEE)
print("Tax: $%.2f" % tax)
print("Total Bill: $%.2f" % total_bill)
