

def celsius_to_fahrenheit(celsius):
    f = (celsius * 9/5) + 32
    return round(f, 1)


def fahrenheit_to_celsius(fahrenheit):
    c = (fahrenheit - 32) * 5/9
    return round(c, 1)


print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(100))
print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(98.6))

print("---")


def describe_weather(celsius):
    if celsius >= 30:
        return "Hot"
    elif celsius >= 20:
        return "Warm"
    elif celsius >= 10:
        return "Cool"
    else:
        return "Cold"


print(describe_weather(30))
print(describe_weather(15))
print(describe_weather(5))


print("=" * 50)


=======================================

def get_base_price(size):
    if size == "small":
        return 8
    if size == "medium":
        return 12
    if size == "large":
        return 16
    return 0


def add_toppings_cost(num_toppings):
    return num_toppings * 1.5


def apply_tax(price):
    price = price * 1.13
    return round(price, 2)


def print_order(name, size, toppings):

    base = get_base_price(size)
    top = add_toppings_cost(toppings)

    subtotal = base + top
    total = apply_tax(subtotal)

    print("==============================")
    print("========PIZZA ORDER===========")
    print("==============================")
    print("Customer  :", name)
    print("Size      :", size)
    print("Toppings  :", toppings)
    print("Subtotal  : $" + str(round(subtotal, 2)))
    print("Total     : $" + str(total))
    print("==============================")
    print()


print_order("Sam Rivera", "medium", 3)
print_order("Alex Chen", "large", 1)


def is_good_deal(total):
    if total < 15:
        return True
    return False
