name = str(input("Enter name: "))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = str(input(">>> "))
while choice.upper() != "Q":
    if choice.upper() == "H":
        print("Hello {}".format(name))
    elif choice.upper() == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = str(input(">>> "))
print("Finished.")
