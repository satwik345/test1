passwords=()

while True:
    print('''
   ------------------------- PASSWORD MANAGER -----------------------------
    1) ADD A PASSWORD
    2) VIEW ALL PASSWORDS
    3) EXIT
    -----------------------------------------------------------------------
    ''')

    c=int(input("Enter your choice(1/2/3): "))
    if c==1:
        website = input("Enter your website: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        a = (website, username, password)
        passwords=passwords+a
        print("Password added")


    elif c==2:
       if len(passwords)==0:
           print("No passwords added")
           break
       for password in passwords:
           print(f"website: {passwords[0]}, username: {password[1]}, password: {password[2]}")


    elif c==3:
        break

    else:
        print("Invalid choice")