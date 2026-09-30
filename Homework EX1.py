land = float(input('Price of the land?: '))
building = float(input('Price of the building?: '))

#21% VAT
total_cost = land + building + ((land + building) * 0.21)
print(f'The total cost of the project is: {total_cost}')

