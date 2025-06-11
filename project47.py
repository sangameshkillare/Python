print('_____________ _______________________ _______________ __________________ ')
print()
print("                 Welcome to the Sudoku Ice-Cream Parlor")
print("_____________ _______________________ _______________ __________________")

# Menu data
all_products_price = {
    1: {'name': 'Chocolate', 'single': 100 ,'Double':190,'Full-rich':500},
    2: {'name': 'Belgium', 'single': 100 ,'Double':190,'Full-rich':500},
    3: {'name': 'Malai', 'single': 100 ,'Double':190,'Full-rich':500},
    4: {'name': 'Strawberry', 'single': 100 ,'Double':190,'Full-rich':500},
    5: {'name': 'Pineapple', 'single': 100 ,'Double':190,'Full-rich':500},
    6: {'name': 'Mix', 'single': 100 ,'Double':190,'Full-rich':500},
    7: {'name': 'Blueberry', 'single': 100 ,'Double':190,'Full-rich':500},

}

def show_menu():
    print('\n\n____________----------- This is our menu --------------____________\n')
    for id, data in all_products_price.items():
        print(f"{id}. {data['name']} Ice Cream (Single, Double, Rich) - Rs. {data['single','Double','Full-rich']}")



def operations():

    print("____________________________________________________________")
    print("\nChoose an operation:")
    print("1: Add Item")
    print("2: Cancel Buying")
    print("3: Show Cart")
    print("4: Remove Item")
    print("5: Checkout and Exit")
    print("____________________________________________________________")
    
def main(): 
    cart = {}

    while True:
        operations()
        try:
            op = int(input("\nEnter operation number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if op == 1:
            show_menu()
            try:
                item_id = int(input("\nEnter the item ID to buy: "))
                quantity = int(input("Enter quantity: "))
                if item_id in all_products_price:
                    if item_id in cart:
                        cart[item_id] += quantity
                    else:
                        cart[item_id] = quantity
                    print(f"{all_products_price[item_id]['name']} x{quantity} added to cart.")
                else:
                    print("Invalid item ID.")
            except ValueError:
                print("Please enter valid numbers.")
        elif op == 2:
            print("Order cancelled. Exiting.")
            break
        elif op == 3:
            if not cart:
                print("Your cart is empty.")
            else:
                print("\nYour Cart:")
                total = 0
                for item_id, quantity in cart.items():
                    item = all_products_price[item_id]
                    item_total = item['price'] * quantity
                    total += item_total
                    print(f"- {item['name']} x{quantity} = Rs. {item_total}")
                print(f"Total: Rs. {total}")
        elif op == 4:
            if not cart:
                print("Cart is empty. Nothing to remove.")
            else:
                try:
                    remove_id = int(input("Enter the item ID to remove: "))
                    if remove_id in cart:
                        del cart[remove_id]
                        print("Item removed from cart.")
                    else:
                        print("Item not in cart.")
                except ValueError:
                    print("Invalid input.")
        elif op == 5:
            print("\nCheckout Summary:")
            total = 0
            for item_id, quantity in cart.items():
                item = all_products_price[item_id]
                item_total = item['price'] * quantity
                total += item_total
                print(f"- {item['name']} x{quantity} = Rs. {item_total}")
            print(f"Total Bill: Rs. {total}")
            print("Thank you for visiting Sudoku Ice Cream Parlor!")
            break
        else:
            print("Invalid operation number.")

# Run the program
main()