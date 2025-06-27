queue=[]
#enque
while True:
    a = int(input("Enter a value to insert: "))
    queue.append(a)
    b = input("want to add more(y/n): ").lower()
    if b == "n":
        break
    elif b != "y":
        print("Invalid input")
print(queue)

#dequeue
if len(queue) == 0:
    print("queue is empty / underflow condition.")
else:
    queue.pop(0)
    print(f"After pop function {queue}.")

#peek
if len(queue) == 0:
    print("queue is empty / underflow condition.")
else:
    print(f"Top element is {queue[0]}.")
