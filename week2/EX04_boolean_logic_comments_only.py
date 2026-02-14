age = int(input("Age: ").strip())
swim = input("can you swim (yes/no): ").lower()

print()  # blank line

# AND: both must be true
if age >= 10 and swim == "yes":
    print("You may enter.")
else:
    print("You may NOT enter.")
