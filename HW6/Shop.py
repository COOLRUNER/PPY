def Load():
    try:
        with open("List.txt", 'r') as f:
            shopping_list = {}
            for line in f:
                item, quantity = line.strip().split('\t')
                shopping_list[item] = quantity
            return shopping_list
            print("List loaded successfully")
    except FileNotFoundError:
        with open("List.txt", 'w') as f:
            return {}
        print("List createds successfully")


def Add(item, quantity):
    shopping_list = Load()
    if item not in shopping_list:
        shopping_list[item] = quantity
        with open("List.txt", 'a') as f:
            f.write(f"{item}\t{quantity}\n")
            print(f"{item} added to the list")


def Remove(item):
    shopping_list = Load()
    if item in shopping_list:
        del shopping_list[item]
        with open("List.txt", 'w') as f:
            for item_, quantity in shopping_list.items():
                f.write(f"{item_}\t{quantity}\n")
    print(f"{item} removed from the list")


def Display():
    shopping_list = Load()
    for item, quantity in shopping_list.items():
        print(f"{item}: {quantity}")


Remove("Bread")
