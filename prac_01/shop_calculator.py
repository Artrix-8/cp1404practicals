
n_items = int(input("Number of items: "))
while n_items < 0:
    print("Invalid number of items!")
    n_items = int(input("Number of items: "))
price_total = 0
for i in range(0, n_items, 1):
    price_total += float(input("Price of item: "))
if price_total > 100:
    price_total *= 0.9

print("Total price of {} items is ${:.2f}".format(n_items, price_total))
