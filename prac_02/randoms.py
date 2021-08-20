import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
line 1: 12, 10, 11, 18
        smallest = 5, largest = 20
line 2: 7, 7, 7, 9
        smallest = 3, largest = 9, 4 would be an impossible output
line 3: 5.268687593587135, 5.305677204957602, 3.5432460832426553, 5.372285501404381
        smallest = 2.5, largest = 5.5
"""

print(random.randint(1, 100))  # unsure of the meaning of "inclusive"
