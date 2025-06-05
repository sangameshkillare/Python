from datetime import datetime

def view_plan():
    print("\nAvailable Wi-Fi Plans:")
    print("1. Basic Plan    | Speed: 50 Mbps  | Subscription: Monthly   | Benefits: Basic Support         | Price: 800")
    print("2. Standard Plan | Speed: 100 Mbps | Subscription: Quarterly | Benefits: Premium Support       | Price: 2,000")
    print("3. Premium Plan  | Speed: 200 Mbps | Subscription: Yearly    | Benefits: OTT, Premium Support  | Price: 6,500")
    print("4. Ultra Plan    | Speed: 500 Mbps | Subscription: Yearly    | Benefits: All Features Included | Price: 12,000")


def suggest_plan():
    print()
    print()
    print()
    print("Enter your requirements. Based on this, we will suggest the best plan for you:")
    print()
    
    speed = int(input("Enter the speed in Mbps: "))
    print()
    print()
    
    subscription = input("Enter the subscription (Monthly/Quarterly/Yearly): ").lower()

    if speed <= 50 and subscription == "monthly":
        print("Suggested plan: Basic Plan")
        return 1, 800
    elif speed <= 100 and subscription == "quarterly":
        print("Suggested plan: Standard Plan")
        return 2, 2000
    elif speed <= 200 and subscription == "yearly":
        print("Suggested plan: Premium Plan")
        return 3, 6500
    elif speed <= 500 and subscription == "yearly":
        print("Suggested plan: Ultra Plan")
        return 4, 12000
    else:
        print("No match found. Please enter valid entries or call our support executive on 1800-00810-520.")
        return 1, 800



#invoice____________________________________________________________________________________________________________________



def generate_invoice(name, Mobile_number, address, plan_name, plan_speed, subscription, benefits_of, price):

    tv_set=input("If you want tv set then enter yes or No (*Note-Extra charges may applicaple) : ")
    
    
    gst = price * 0.18
    installation=999
    if tv_set =="yes":
        charges=599
        with_gst=599*0.18
        total_price = price + gst+with_gst +installation       
    else:
        print("Please enter valid choise (in yes?No):")
        total_price=price+gst+installation
    # gst = price * 0.18
    # installation=999
    
    

    print("\n========== Wi-Fi Installation Invoice ==========")
    print(f"Name          : {name}")
    print(f"Mobile Number : {Mobile_number}")
    print(f"Address       : {address}")
    print(f"Plan Selected : {plan_name}")
    print(f"Speed         : {plan_speed}")
    print(f"Subscription  : {subscription}")
    print(f"Benefits      : {benefits_of}")
    print(f"Installation  : {installation}")
    if tv_set==True:
      print(f"Set-top-box   : {charges}")
    print(f"Plan Price    : {price}")
    print(f"GST (18%)     : {gst}")
    print(f"Total Amount  : {int(total_price)}")
    print("Payment Method :  Cash after Installation ")
    print(f"Installation Date: {datetime.now().strftime('%Y-%m-%d')}")
    print("================================================")




# Main Code_______________________________________________________________________________________________________________

print("____________________________________________________________________________________________________________________________")
print("     W   E   L   C   O   M   E  -  T  O   -   G   I   G   A   N   E   T   -   W   I   F  I   -   S  E   R  V   I  C   E")
print("____________________________________________________________________________________________________________________________")
print()
print()
print()

Mobile_number = int(input("Enter the Mobile Number: "))
name = input("Enter your name: ")
address = input("Enter the Installation address: ")

view_plan()

plan_id, price = suggest_plan()
if plan_id is None:
    print("Exiting program.")
    exit()

print("You can go with the suggested plan or select what you want.")


selected_plan = int(input("Enter the plan ID in 1-4 to select a plan and get an invoice: "))

if selected_plan == 1:
    plan_name = "Basic Plan"
    plan_speed = "50 Mbps"
    subscription = "Monthly"
    benefits_of = "Basic Support"
    price = 800
elif selected_plan == 2:
    plan_name = "Standard Plan"
    plan_speed = "100 Mbps"
    subscription = "Quarterly"
    benefits_of = "Premium Support"
    price = 2000
elif selected_plan == 3:
    plan_name = "Premium Plan"
    plan_speed = "200 Mbps"
    subscription = "Yearly"
    benefits_of = "OTT, Premium Support"
    price = 6500
elif selected_plan == 4:
    plan_name = "Ultra Plan"
    plan_speed = "500 Mbps"
    subscription = "Yearly"
    benefits_of = "All Features Included"
    price = 12000
else:
    print("Invalid choice. Defaulting to Ultra Plan.")
    plan_name = "Ultra Plan"
    plan_speed = "500 Mbps"
    subscription = "Yearly"
    benefits_of = "All Features Included"
    price = 12000

# Call the function to generate the invoice
generate_invoice(name, Mobile_number, address, plan_name, plan_speed, subscription, benefits_of, price)

print()
print()
print()
print()

print(" YOUR ORDER IS PLACED SUCCESSFULLY , PAYMENT METHOD IS  BY DEFAULTLY - CASH AFTER INSTALLATION ")
print("OUR TECHNICIAN WILL CALL YOU  IN 1 - 2 WORKING DAYS .")



print("____________________________________________________________________________________________________________________________")
print("                                              T  H  A  N  K  -  Y  O  U                                           ")
print("____________________________________________________________________________________________________________________________")
