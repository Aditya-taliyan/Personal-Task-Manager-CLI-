from task_manager import database, display
from datetime import datetime

def run():
    database.create_table()

    while True:
        display.show_menu()
        choice = input("Choose an option (1-5):")

        if choice == '1':
            title = input("Enter the title").strip()

            if title =="":
                display.show_message("title can not be empty .Task not added")
                continue

            priority = input("Enter the priority (High/Medium/low) [default Medium]:").strip()
            if priority == '':
                priority = "Medium"
            elif priority not in ["High" , "HIGH" , "high" , "Medium" , "MEDIUM" , "medium" , "Low" , "LOW" , "low"]:
                display.show_message("Invalid priority. Task not added.")
                continue

            due_date = input("Enter the due date (YYYY-MM-DD) [optional]:").strip()
            if due_date=="":
                due_date=None
            else:
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                except ValueError:
                    display.show_message("Invalid date format. Task not added")
                    continue
                    
            database.add_task(title,priority,due_date)
            display.show_message("Task added successfully")


        elif choice =='2':
            rows = database.get_all_tasks()
            display.show_tasks(rows)
        
        elif choice =='3':
            rows = database.get_all_tasks()
            display.show_tasks(rows)
            try :
                task_id = int(input("Enter task ID to delete: "))
            except ValueError:
                display.show_message("Enter the integer value")
                continue
            database.delete_tasks(task_id)
            display.show_message("Task deleted successfully.")
        
        elif choice== '4':
            rows = database.get_all_tasks()
            display.show_tasks(rows)
            try:
                task_id = int(input("Enter task ID to mark as done: "))
            except ValueError:
                display.show_message("Enter the Task_id")
                continue
            database.mark_done(task_id)
            display.show_message("Task marked as done.")

        elif choice =='5':
            display.show_message("Goodbye!")
            break

        else:
            display.show_message("Invalid choice , try again.")