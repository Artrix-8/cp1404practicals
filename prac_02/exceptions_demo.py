try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1. ValueError occurs when you input a non-integer number
2. ZeroDivisionError occurs when the user inputs 0 for the denominator
3. Unsure what this question is asking for
"""