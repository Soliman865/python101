hot = input("Do you want something hot? (yes/no)").strip().lower() == "yes"
healthy = input("Do you want something healthy? (yes/no)").strip().lower() == "yes"
if hot and healthy:
    print("You should eat soup")
elif hot and (not healthy):
    print("you should eat pizza")
elif (not hot) and healthy:
    print("you should eat salad")
elif (not hot) and (not healthy):
    print("you should eat sandwich")
