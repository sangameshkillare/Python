import json

class task:
    def __init__(self,task_id,task_name,task_description,status,start_date,due_date,amount=None):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.status = status
        self.start_date = start_date
        self.due_date = due_date
        self.amount = amount
    
    def __str__(self):
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Description: {self.task_description}, Status: {self.status}, Start Date: {self.start_date}, Due Date: {self.due_date}, Amount: {self.amount}"
    
    
class taskmanager:
    
    def __init__(self):
        self.tasks=[]
        print(self.tasks)
        
        
    def add_task(self):
        
        try:
            task_id = int(input("Enter task ID: "))
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            status = input("Enter task status: ")
            start_date = input("Enter start date (DD-MM-YYYY): ")
            due_date = input("Enter due date (DD-MM-YYYY): ")
            amount = float(input("Enter amount (optional, press Enter to skip): ") or 0)
        
            new_task = task(task_id,task_name,task_description,status,start_date,due_date,amount)
            self.tasks.append(new_task)
            print(f"Task '{task_name}' added successfully.")    
            
    
        
        except ValueError as e:
            print(f"Invalid input:{e} please try again")
        
        
    def view_tasks(self):
        for task in self.tasks:
            print(task)
        
    def read_task(self,task_id):
        for task in self.tasks:
            if task.task_id==task_id:
                print(task)
                return
        print(f"Task with ID {task_id} not found.")
        
    def upadate(self):
        if not self.tasks:
            print("No tasks available to update.")
            return
        print("----------all tasks----------")
        self.view_tasks()
        
        
        try:
            selected_id = int(input("Enter the task ID to update: "))
    
        except ValueError:
            print("Invalid input. Please enter a valid task ID.")
            return
        
    
        for task in self.tasks:
           if task.task_id == selected_id:
            selected_task = task
            print('task found')
            print(selected_task)
            print()
            
            print("_______________select the feild to update_______________")
            print("\n-------- Update Menu --------")
            print("1. Amount")
            print("2. Status")
            print("3. Start Date")
            print("4. Due Date")
            print("5. Task Name") 
            print("6. Task Description")
            print("7. Exit")
            
            choice = input("Enter your choice (1-7): ").strip()
            if choice == '1':
                try:
                    selected_task.amount = float(input("Enter new amount: "))
                except ValueError:
                    print("Invalid amount.")
                    
            elif choice == '2':
                selected_task.status = input("Enter new status: ")
            elif choice == '3':
                selected_task.start_date = input("Enter new start date (DD-MM-YYYY): ")
            elif choice == '4':
                selected_task.due_date = input("Enter new due date (DD-MM-YYYY): ")
            elif choice == '5':
                selected_task.task_name = input("Enter new task name: ")
            elif choice == '6':
                selected_task.task_description = input("Enter new task description: ")
            elif choice == '7':
                print("Exiting update menu.")
                
            else:
                print("Invalid choice.")
                
            print("Task updated successfully.")
            
       
        
        
        
    def delete(self,task_id):
        try:
            for task in self.tasks:
             if task.task_id==self.task_id:
                self.task.remove(task)
                print(f"Task '{task.task_name}' deleted successfully.")
                return
            print(f"Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Invalid input: {e} please try again")
   
    
  
manager=taskmanager()


print("Welcome to the Task Manager!")
print('Do you eant to enter in the Editing mode.')




while True:
    print("#-------------please select an option-------------#")
    print("1. Add Task")
    print("2. View Tasks")  
    print("3. Read Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ").strip() 
    
    if choice=='1':
        manager.add_task()
    elif choice=='2':
        manager.view_tasks()
    elif choice=='3':
        try:
            manager.read_task(int(input("Enter task ID to read: ")))
        except ValueError:
            print("Invalid task ID. Please enter a valid integer.")
    elif choice=='4':
        manager.upadate()   
    elif choice=='5':
        manager.delete(input("Enter task ID to delete:" ))
    elif choice=='6':
        print("Exiting the task manager.")
        break
    
