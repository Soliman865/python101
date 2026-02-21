num = int(input("Enter 1-10: "))

while True:
    if num < 1 or num > 10:
        print("Invalid, try again.")
        num = int(input("Enter 1-10: "))
        continue   
    print("Accepted!")
    break          
