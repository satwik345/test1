stack=[]
#push
while True:
    a = int(input("Enter a value to insert: "))
    stack.append(a)
    b = input("want to add more(y/n): ").lower()
    if b == "n":
        break
    elif b != "y":
        print("Invalid input")
print(stack)

#pop
if len(stack) == 0:
    print("stack is empty / underflow condition.")
else:    
    stack.pop()
    print(stack)

#peek
if len(stack) == 0:
    print("stack is empty / underflow condition.")
else:
    top=stack.pop()
    print(f"Top elememt is {top}.")
