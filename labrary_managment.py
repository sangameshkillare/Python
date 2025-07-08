class task:
    def __init__(self, task_id, task_name, task_description,status="Pending"   ,due_date=None):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.status = status
        self.due_date = due_date

    def __str__(self):
        return f"Task ID: {self.task_id}, Name: {self.task_name}, Description: {self.task_description}, Status: {self.status}, Due Date: {self.due_date}"

class taskmanager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.task_name}' added successfully.")

    def view_tasks(self):
        for task in self.tasks:
            print(task)
        
    def read_task(self,task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                print(task)
                return
        print(f"Task with ID {task_id} not found.")

    def update_task(self, task_id, status=None, due_date=None, task_name=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if status:
                    task.status = status
                if due_date:
                    task.due_date = due_date
                if task_name:
                    task.task_name = task_name
                print(f"Task '{task.task_name}' updated successfully.")
                return
        print(f"Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task '{task.task_name}' deleted successfully.")
                return
        print(f"Task with ID {task_id} not found.")
        
    
manager=taskmanager()
manager.add_task(task(1, "Complete Assignment", "Finish the math assignment by tomorrow", "Pending", "2023-10-15"))
manager.add_task(task(2, "Grocery Shopping", "Buy groceries for the week", "Pending", "2023-10-16"))
# manager.view_tasks()

manager.update_task(1, status="Completed", due_date="2023-10-14",task_name="Complete Math Assignment")
# manager.view_tasks()
manager.read_task(1)
# manager.delete_task(2)