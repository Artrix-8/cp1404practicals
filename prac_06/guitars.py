"""yep"""

from prac_06.guitar import Guitar

print("My Guitars!")
guitars = []

name = input("Name: ")

# for testing:
if name == "":
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    # error check to insure number is inputted
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(guitar, "added")
    print("")
    name = input("Name: ")  # begins new loop if string is inputted

print("")
print('... snip ...')
print("")

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
