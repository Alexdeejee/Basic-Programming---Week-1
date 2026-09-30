print("*** welcome to the checkout system ***")

trousers = int(input("How many pairs of trousers have been bought? "))
t_shirts = int(input("How many T-shirts have been bought? "))
vests = int(input("How many vests have been bought? "))

total = trousers * 70.5 + t_shirts * 20.89 + vests * 100.3

print("You have bought")
print(f"Trousers: {trousers} pair(s)")
print(f"T-shirts: {t_shirts} piece(s)")
print(f"Vests: {vests} piece(s)")
print(f"Total: {total:.2f}")