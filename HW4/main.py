import random


# def password_generator():
#     print("Enter the type of characters you want to use: D for digits, L for letters, S for special characters")
#     type_ = input()
#     if type_ not in ['D', 'L', 'S']:
#         print("Invalid type")
#         return
#     print("Enter specific characters you want to exclude")
#     specific = input()
#     print("Enter the length of the password")
#     length = int(input())
#     if length < 8:
#         print("Password is too short")
#         return
#     if type_ == 'D':
#         characters = [str(x) for x in range(0, 10)]
#
#     if type_ == 'L':
#         characters = [chr(x) for x in range(65, 91)] + [chr(x) for x in range(97, 123)]
#
#     if type_ == 'S':
#         characters = ['@', '#', '$', '%', '&', '*']
#
#     # Remove specific characters from the list
#     for char in specific:
#         if char in characters:
#             characters.remove(char)
#
#     password = ''
#     for i in range(length):
#         password += str(random.choice(characters))
#     print(password)
#
#     print("Do you want to generate another password? Y/N")
#     answer = input()
#     if answer == 'Y':
#         password_generator()
#     else:
#         return
#
#
# password_generator()

def order_pizza(*toppings, **kwargs):
    print("Enter the size of the pizza: S for small, M for medium, L for large")
    size = input()
    print("Enter the type of crust: thin or thick")
    crust = input()
    print("Enter the toppings for the pizza, separated by commas")
    toppings = input().split(',')

    # Calculate the base price
    if size == 'S':
        price = 10
    elif size == 'M':
        price = 15
    elif size == 'L':
        price = 20
    else:
        print("Invalid size")
        return
    if crust == 'thick':
        price += 3
    elif crust != 'thin':
        print("Invalid crust type")
        return
    if len(toppings) < 2:
        print("You must choose at least 2 toppings")
        return
    elif len(toppings) > 7:
        print("You can choose up to 7 toppings")
        return
    else:
        price += max(0, len(toppings) - 2) * 2
    print(f"Your order: {size} pizza with {', '.join(toppings)} on {crust} crust. Total price: {price}")
    print("Do you want to order another pizza? Y/N")
    answer = input()
    if answer == 'Y':
        order_pizza()

order_pizza()
