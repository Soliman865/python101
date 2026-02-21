choice = input("Choose a/b/c/q: ").strip().lower()
while choice != "q":
    print("Goodbye")
    if choice == "a":
        print("hello")
    elif choice == "b":
        number = int(input("give me a number"))
        print(number * number)
    elif choice == "c":
        word = input("Type a word: ").strip()

        a,e,i,o,u = 0
        for ch in word.lower():
            if ch in "aeiou":
                a,e,i,o,u = a,e,i,o,u + 1

        print("a,e,i,o,u =",a,e,i,o,u)
    else:
        print("invalid choice")
