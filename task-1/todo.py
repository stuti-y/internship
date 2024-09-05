# Initialize an empty list to store tasks
tasks = []

# Function-1 to display the to-do list
def display_tasks():
    if not tasks:  # Check if the task list is empty
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            # Determine the status of each task (Done/Not Done)
            status = "Done" if task["completed"] else "Not Done"
            # Display task with priority and color coding
            print(f"{i}. {task['task']} - Priority: {task['priority']} ({status}) - Color: {task['color']}")

# Function-2 to add a task to the to-do list
def add_task(task_name, priority, color):
    tasks.append({"task": task_name, "completed": False, "priority": priority, "color": color})
    print(f"Task '{task_name}' with priority '{priority}' and color '{color}' added to your to-do list.")

# Function-3 to mark a task as completed
def mark_completed(task_number):
    if 1 <= task_number <= len(tasks):  # Validate the task number
        tasks[task_number - 1]["completed"] = True  # Mark the task as completed
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function-4 to remove a task from the to-do list
def remove_task(task_number):
    if 1 <= task_number <= len(tasks):  # Validate the task number
        removed_task = tasks.pop(task_number - 1)  # Remove the task from the list
        print(f"Task '{removed_task['task']}' removed from your to-do list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function-5 to organize tasks by priority
def organize_by_priority():
    tasks.sort(key=lambda x: x["priority"])  # Sort tasks by priority
    print("Tasks organized by priority.")

# Function-6 to update task color
def update_task_color(task_number, color):
    if 1 <= task_number <= len(tasks):  # Validate the task number
        tasks[task_number - 1]["color"] = color  # Update the task color
        print(f"Task {task_number} color updated to '{color}'.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main function to control the program flow
def main():
    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Remove a task")
        print("5. Organize tasks by priority")
        print("6. Update task color")
        print("7. Quit")

        choice = input("Enter your choice: ").strip()  # Get user choice

        if choice == '1':
            display_tasks()  # Display the to-do list
        elif choice == '2':
            task_name = input("Enter the task: ").strip()  # Get the new task name
            priority = int(input("Enter the priority (1-5): ").strip())  # Get the task priority
            color = input("Enter the color: ").strip()  # Get the task color
            add_task(task_name, priority, color)  # Add the new task
        elif choice == '3':
            display_tasks()  # Display the to-do list for reference
            try:
                task_number = int(input("Enter the task number to mark as completed: ").strip())  # Get the task number
                mark_completed(task_number)  # Mark the task as completed
            except ValueError:
                print("Invalid input. Please enter a valid task number.")  # Handle invalid input
        elif choice == '4':
            display_tasks()  # Display the to-do list for reference
            try:
                task_number = int(input("Enter the task number to remove: ").strip())  # Get the task number
                remove_task(task_number)  # Remove the task
            except ValueError:
                print("Invalid input. Please enter a valid task number.")  # Handle invalid input
        elif choice == '5':
            organize_by_priority()  # Organize tasks by priority
        elif choice == '6':
            display_tasks()  # Display the to-do list for reference
            try:
                task_number = int(input("Enter the task number to update color: ").strip())  # Get the task number
                color = input("Enter the new color: ").strip()  # Get the new task color
                update_task_color(task_number, color)  # Update the task color
            except ValueError:
                print("Invalid input. Please enter a valid task number.")  # Handle invalid input
        elif choice == '7':
            break  # Exit the loop and quit the program
        else:
            print("Invalid choice. Please enter a valid option.")  # Handle invalid menu choice

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function
