# # Welcome 
# # Menu 
# # Add dish 
# # Name of dish and bill . 
# # And 10 per discount for above 1000
# # Thank you
# # Step 1: Welcome Message
# print("Welcome to the Restaurant!")
# print("We are delighted to serve you!")
# print("-" * 30)


# # Step 2: Menu and Dish Selection
# menu = {
#     "burger": 50,
#     "pizza": 150,
#     "pasta": 120,
#     "fries": 40,
#     "coke": 30,
# }

# print("___________Menu___________")
# for items,price in menu.items():
#     print(f"{items}:{price}")
# print("________________________")

# selected_items=[]
# while True:
#     dish=input("Enter Dish name :- (done for exit if you selected the items :) :")
#     if dish =="done":
#         break
#     elif dish in menu:
#         quantity=int(input("Enter the quantity :"))
#         selected_items.append((dish,menu[dish],quantity))
#     else:
#         print("Invalid Choise :")


# print (selected_items)


# print("___________Your bill__________")
# print(f"{'items':<15}{"price":<10}{'quantity':,")