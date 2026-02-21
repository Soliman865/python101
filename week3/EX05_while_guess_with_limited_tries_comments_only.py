secret = 9
        tries_left = 4
        attempts = 0

        while tries_left > 0:
            guess = int(input("Enter a number between 1 and 10: "))
            attempts += 1
            tries_left -= 1

            if guess == secret:
                print("Nice job!")
                break
            elif guess > secret:
                print("Too high, try again.")
            else:
                print("Too low, try again.")

        if guess != secret:
            print("You ran out of tries the correct answer was", secret)
