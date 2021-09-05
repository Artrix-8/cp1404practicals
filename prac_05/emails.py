"""
Program to store users name and email
"""

email_to_name = {}
email = input("Email: ")
while email != "":
    name_in_parts = (email.split('@')[0]).split('.')
    name = " ".join(name_in_parts).title()
    choice = input(f"Is your name {name}? (Y/n) ")
    if choice.lower() != "y" and choice != "":
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")
for email, name in email_to_name.items():
    print(f"{name} ({email})")
