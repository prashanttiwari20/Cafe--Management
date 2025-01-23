#Define the menu of resturant
menu = {
'Pizza':40,
'Pasta' :50,
'Burger':60,
'Salad' :70,
'Coffee': 30,
'cold Coffee':90,
}

#Greet
print("Welcome to Mit Cafe")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs30\nCold Coffee: Rs 90")

order_Total = 0

item_1 = input("Enter the name of item you want to order =")
if item_1 in  menu:
    order_Total += menu[item_1]
    print(f"Your item{item_1}has been added to your order")

else:
    print(f"Ordered item {item_1}is not avilable yet!")

another_order = input("Do you want to add another item? (yes/No)")

if another_order == "yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_Total += menu[item_2]
        print("item{item_2} has been added to order")
    else:
        print(f"Ordered item{item_2} is not avilable!")

print(f"THE TOTAL AMOUNT OF ITEMS TO PAY IS {order_Total}")