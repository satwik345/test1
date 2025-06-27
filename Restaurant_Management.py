menu={"APPETIZERS":( "VEG MANCHURIAN","PANNER TIKKA","BABY CORN FRY","FISH FRY(BONELESS)","CHICKEN FRY","CHICKEN TANDOORI"," CHICKEN LOLIPOP","CHICKEN MANCHURIAN"),
      "MAIN COURSE":("CHICKEN/PANNER/MUSHROOM BIRYANI","FRIED RICE","VEG THALI","NON VEG THALI"),
      "DESSERTS":("ICE CREAM","GULAB JAMUN")}
table_numbers=[1,2,3,4,5,6,7,8,9,10]

while True:
        print('''
        --------------RESTAURANT RESERVATION-------------------
        1)TABEL RESERVATION
        2)CANCEL RESERVATION
        3)MENU
        4)EXIT
        -------------------------------------------------------
        ''')
        i=int(input("ENTER YOUR CHOICE(1/2/3): "))


        if i == 1:
            if len(table_numbers) == 0:
                print("SORRY NOT AVAILABLE AT PRESENT!")
            else:
                table_reserved = table_numbers.pop(0)
                print("RESERVATION COMPLETE.")
                print(f"RESERVATION NUMBER: {table_reserved}.")
                b=input("WANT TO EXIT (Y/N): ").lower()
                if b=="y":
                    break
                elif b== "n" or "y":
                    print("INVALID INPUT.")
        elif i == 2:
            a=int(input("ENTER YOUR RESERVATION NUMBER: "))
            if 1<=a and not a >= 10:
                table_numbers.append(a)
                print("YOUR RESERVATION HAS BEEN CANCELLED SUCCESSFULLY.")
                C = input("WANT TO EXIT (Y/N): ").lower()
                if C == "y":
                    break
                elif C == "n" or "y":
                    print("INVALID INPUT.")
        elif i == 3:
            print(menu)
            D = input("WANT TO EXIT (Y/N): ").lower()
            if D == "y":
                break
            elif D == "n" or "y":
                print("INVALID INPUT.")
        elif i == 4:
            break
        else:
            print("INVALID CHOICE!")
