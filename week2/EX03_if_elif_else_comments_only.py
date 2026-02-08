# In Python, the input() function always returns a string (text), even if you type a number. You cannot compare a string to an integer using >=.
    t = int(input("Give me a temperature in Celsius "))

    if t >= 25:
        print("Hot")
    elif t >= 15:
        print("Warm")
    elif t >= 5:
        print("Cool")
    else:
        print("Cold")
