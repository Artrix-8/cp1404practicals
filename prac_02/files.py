
name = str(input("Pls enter your name: "))
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

in_file = open('name.txt', 'r')
name_read = in_file.readline()
print(f"Your name is {name_read}")
in_file.close()

in_file = open('numbers.txt', 'r')
num1 = in_file.readline()
num2 = in_file.readline()
total = int(num1) + int(num2)
print(f"Sum of values is {total}")
in_file.close()

in_file = open('numbers.txt', 'r')
total = 0
n_lines = 0
for line in in_file:
    total += int(line)
    n_lines += 1
print(f"Sum of {n_lines} numbers is {total}")
in_file.close()
