usr = input("Enter your name: ")
msg = input("Enter your message: ")
with open("vault.txt", "a") as vault:
    vault.write("\n" + "User: " + str(usr) + " | Message: " + str(msg))
