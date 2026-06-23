def show_menu():
    print("\n" + "="*40)
    print("           PERSONAL TASK MANAGER")
    print("="*40)
    print("  1. Add task")
    print("  2. View All Task")
    print("  3. Delete Task")
    print("  4. Mark Task As Done")
    print("  5. Exit")
    print("="*40)

def show_tasks(rows):
    if not rows:
        print("\n No tasks found")
        return
    
    print("\n"+ "="*60)
    print(f" {'ID':<5} {'TITLE':<20} {'PRIORITY':<10}{'DUE DATE':<12} {'DONE'}")
    print("="*60)

    for row in rows:
        id, title, priority, due_date , done = row
        status ="✓" if done else "x"
        due = due_date if due_date else "No date"
        print(f" {id:<5} {title:<20} {priority:<10} {due:12} {status}")
    
    print("="*60)

def show_message(msg):
    print(f"\n >>{msg}")
