
def main():
    numbers = get_numbers()
    print_number_facts(numbers)
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter username: ")
    determine_access(username, usernames)


def determine_access(username, usernames):
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def print_number_facts(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The largest number is {sum(numbers) / len(numbers)}")


def get_numbers():
    numbers = []
    for i in range(5):
        numbers.append(float(input("Number: ")))
    return numbers


main()
