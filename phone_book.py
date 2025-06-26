phone_book={}
while True:

    print('''
    ----------------------PHONE BOOK--------------------------------
    1)ADD NUMBER
    2)DISPLAY NUMBERS
    3)EXIT
    ----------------------------------------------------------------
    ''')
    C = int(input("ENTER YOUR CHOICE (1/2/3): "))

    if C == 1:
        name = input("Enter your name: ")
        number = input("Enter your number: ")
        phone_book[name] = number
        print("Phone number has been added")
        while True:
            d=input("Do you want to add another number? (y/n): ").lower()
            if d == "y":
                name = input("Enter your name: ")
                number = input("Enter your number: ")
                phone_book[name] = number
                print("Phone number has been added")
            elif d == "n":
                break
            else:
                print("Invalid input")

    elif C == 2:
        if len(phone_book)==0:
            print("Empty phone book")
        else:
             print(phone_book)

    elif C == 3:
        break

    else:
        print("Invalid input")