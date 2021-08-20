x = int(input("Enter smaller number (x): "))
y = int(input("Enter larger number (y): "))

"""
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))
"""

# print even numbers
print("Even numbers from {} to {}:".format(x, y))
if (x % 2) == 0:
    for i in range(x, y+1, 2):
        print(i, end=' ')
else:
    for i in range(x+1, y+1, 2):
        print(i, end=' ')
print()

# print odd numbers
print("Odd numbers from {} to {}:".format(x, y))
if (x % 2) != 0:
    for i in range(x, y+1, 2):
        print(i, end=' ')
else:
    for i in range(x+1, y+1, 2):
        print(i, end=' ')
print()

# print square numbers
print("Squares from {} to {}:".format(x, y))
for i in range(x, y+1, 1):
    print(i*i, end=' ')
