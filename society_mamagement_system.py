# import json

# class bill:
#     def __init__(self,bill_id,bill_name,bill_description,status,start_date,due_date,amount=None):
#         self.bill_id = bill_id
#         self.bill_name = bill_name
#         self.bill_description = bill_description
#         self.status = status
#         self.start_date = start_date
#         self.due_date = due_date
#         self.amount = amount
        
#     def __str__(self):
#         return f"bill ID: {self.bill_id}, Name: {self.bill_name}, Description: {self.bill_description}, Status: {self.status}, Start Date: {self.start_date}, Due Date: {self.due_date}, Amount: {self.amount}"
    
    
# class taskmanager:
    
#     def __init__(self):
#         self.bills=[]
#         # print(self.bibill
        
        
#     def add_bill(self):
#         confirm=input('Do you want to add a bill? (yes/no): ').strip().lower()
        
#         if confirm=='yes':
#             print("Adding a new task...")
            
            
#             try:
            
#                 bill_id = int(input("Enter bill ID: "))
                
#                 if bill_id==0:
#                     raise ValueError("bill ID cannot be zero.")
                
#                 bill_name = input("Enter bill name: ")
#                 bill_description = input("Enter bill description: ")
#                 status = input("Enter bill status: ")
#                 start_date = input("Enter start date (DD-MM-YYYY): ")
#                 due_date = input("Enter due date (DD-MM-YYYY): ")
#                 amount = float(input("Enter amount (optional, press Enter to skip): ") or 0)
        
#                 new_bill = bill(bill_id,bill_name,bill_description,status,start_date,due_date,amount)
#                 self.bills.append(new_bill)
#                 print(f"Task '{bill_name}' added successfully.")    
            
    
        
#             except ValueError as e:
#                 print(f"Invalid input:{e} please try again")
          

            
#         elif confirm=='no'or confirm!='yes':
#             print("Bill addition cancelled.")
           
        
        
#     def view_bills(self):
#         for bill in self.bills:
#             print("This is the list of bills :- ")
#             print("_________________________________________________________")   
#             print() 
#             print(f"bill_id -{bill.bill_id} | bill_name-{bill.bill_name} | bill_Description-{bill.bill_description} | bill_status-{bill.status} | Task_Start_date-{bill.start_date} | bill_end_date-{bill.due_date} | Task_amount-{bill.amount}|")
#             print("_________________________________________________________")
            
            
                    
#     def read_bill(self,bill_id):
#         for bill in self.bills:
#             if bill.bill_id==bill_id:
#                 print(bill)
#                 return
#         print(f"Task with ID {bill_id} not found.")
        
        
        
#     def upadate(self):


#         try:
#             selected_id = int(input("Enter the task ID to update: "))
    
#         except ValueError:
#             print("Invalid input. Please enter a valid task ID.")
#             return
        
    
#         for bill in self.bills:
#           if bill.bill_id == selected_id:
#             selected_bill = bill
#             print('task found')
#             print(selected_bill)
#             print()
            
#             print("_______________select the feild to update_______________")
#             print("\n-------- Update Menu --------")
#             print("1. Amount")
#             print("2. Status")
#             print("3. Start Date")
#             print("4. Due Date")
#             print("5. Bill Name") 
#             print("6. Bill Description")
#             print("7. Exit")
            
#             choice = input("Enter your choice (1-7): ").strip()
#             if choice == '1':
#                 try:
#                     selected_bill.amount = float(input("Enter new amount: "))
#                 except ValueError:
#                     print("Invalid amount.")
                    
#             elif choice == '2':
#                 selected_bill.status = input("Enter new status: ")
#             elif choice == '3':
#                 selected_bill.start_date = input("Enter new start date (DD-MM-YYYY): ")
#             elif choice == '4':
#                 selected_bill.due_date = input("Enter new due date (DD-MM-YYYY): ")
#             elif choice == '5':
#                 selected_bill.bill_name = input("Enter new bill name: ")
#             elif choice == '6':
#                 selected_bill.bill_description = input("Enter new bill description: ")
#             elif choice == '7':
#                 print("Exiting update menu.")
                
            
                
#             print("Task updated successfully.")
            
       
        
        
        
#     def delete(self,bill_id):
#         try:
#             for bill in self.bills:
#                 if bill.bill_id==bill_id:
#                   self.bills.remove(bill)
#                   print(f"bill '{bill.bill_name}' deleted successfully.")
#                   return
#             print(f"bill with ID {bill_id} not found.")
#         except ValueError as e:
#             print(f"Invalid input: {e} please try again")
  
# manager=taskmanager()


# print("Welcome to the Socity Management System Task Manager")


# while True:
#     print("#-------------please select an option-------------#")
#     print("1. Add Bill")
#     print("2. View Bills")  
#     print("3. Read Bill")
#     print("4. Update Bill")
#     print("5. Delete Bill")
#     print("6. Go to Main Menu")
#     choice = input("Enter your choice (1-6): ").strip() 
    
#     if choice=='1':
#         manager.add_bill()
#     elif choice=='2':
#         manager.view_bills()
#     elif choice=='3':
#         try:
#             manager.read_bill(int(input("Enter bill ID to read: ")))
#         except ValueError and OverflowError:
#             print("Invalid bill ID. Please enter a valid integer.")
#     elif choice=='4':
#         manager.upadate()   
#     elif choice=='5':
#         try:
#              bill_id = int(input("Enter bill ID to delete: "))
#              manager.delete(bill_id)
#         except ValueError:
#              print("Invalid ID. Please enter a number.")

#     elif choice=='6':
#         print("Exiting the bill manager.")
#         break
    
from abc import ABC, abstractmethod

class ATM(ABC):  # Abstract class
    @abstractmethod
    def authenticate(self):
        pass
        print('hello from abstract class')
    @abstractmethod
    def withdraw(self):
        pass

class MyATM(ATM):
    def authenticate(self):
        print("Card and PIN verified.")

    def withdraw(self):
        print("Cash withdrawn.")

atm = MyATM()
atm.authenticate()
atm.withdraw()
