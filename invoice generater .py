# Welcome 
# Menu 
# Add dish 
# Name of dish and bill . 
# And 10 per discount for above 1000
# Thank you


print("Welcome to the Burger King .")
print("Our Menu ---->")


print("1. Burgers")
print("2. Beverages")
print("3. Sides")
print("4. Desserts")

select=int (input("Enter the choise:"))

if select==1:
    print("\nBurger King Product List:")
    print("Burgers:")
 
 
    # print("   1- Whopper")
    # print("   2- Chicken Royale")
    # print("   3- Veggie Burger")
    # print("   4- BBQ Bacon Burger")
    # sub_sel=int(input("Enter the choise :"))
elif select==2:
    print("\nBeverages:")
    print("   1- Coca-Cola")
    print("   2- Sprite")
    print("   3- Iced Tea")
    print("   4- Milkshake")
    
    sub_sel=int(input("Enter the choise :"))
elif select==3:
    print("\nSides:")
    print("   1- French Fries")
    print("   2- Onion Rings")
    print("   3- Chicken Nuggets")
    print("   4- Cheese Sticks")
    
    sub_sel=int(input("Enter the choise :"))
elif select==4:
    print("\nDesserts:")
    print("   1- Chocolate Sundae")
    print("   2- Apple Pie")
    print("   3- Brownie")
    print("   4- Ice Cream Cone")
    
    sub_sel=int(input("Enter the choise :"))
else:
    print("The item you entered is not in the menu , Please enter the Valid item .")