from cryptography.fernet import Fernet

masterPwd = input("Enter the password: ")

def view():
    with open("pwds.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: " + user + " | " + "Pass: " + passw)


def add():
    name = input("Enter the username: ")
    pwd = input("Enter the password: ")
    with open("pwds.txt", "a") as f:
        f.write( str(name) + "|" + str(pwd) + "\n")

while True:
    mode = input("Would you like to view or add to your passwords? (view / add): ").lower()

    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()
    else:
        print("That wasn't an option.")