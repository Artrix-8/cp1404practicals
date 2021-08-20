MIN_PASS = 4


def main():
    password = input(f"Create Password (must be {MIN_PASS} characters long): ")
    while len(password) < MIN_PASS:
        print("Password too short!!!")
        password = input("Enter password of at least {} characters: ".format(MIN_PASS))
    print('*' * len(password))


main()
