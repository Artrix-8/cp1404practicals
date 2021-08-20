MIN_PASS = 4


def main():
    password = get_password()
    print_password_secret(password)


def print_password_secret(password):
    print('*' * len(password))


def get_password():
    password = input(f"Create Password (must be {MIN_PASS} characters long): ")
    while len(password) < MIN_PASS:
        print("Password too short!!!")
        password = input("Enter password of at least {} characters: ".format(MIN_PASS))
    return password


main()
