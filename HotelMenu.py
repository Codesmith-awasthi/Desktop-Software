#Define The Menu of Restaurrant
menu = {
    'Pizza':60,
    'Pavbhaji':80,
    'Red Suase Pasta':40,
    'Salad':70,
    'Maggi':35,
    'Coffee': 80,
    'Burger':60,
}

#Greet
print("Welcome to The Awasthiis Restaurrant")
print("Pizza: Rs40 \nPavbhaji:80,Red Suase Pasta:40\nSalad:70\nMaggi':35\nCoffee': 80\nBurger':60,")

order_total = 0
#80 + 70 =150

item_1 = input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? ( Yes/No) ")
if another_order.lower() == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items is {order_total}")