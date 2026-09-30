print("*** Welcome to the checkout system.***")

trousers = int(input("How many trousers have been bought? "))
t_shirts = int(input("How many T-shirts have been bought? "))
vests = int(input("How many vests have been bought? "))

total = trousers * 70.5 + t_shirts * 20.89 + vests * 100.3

print(f"Total amount to pay: {total:.2f}")