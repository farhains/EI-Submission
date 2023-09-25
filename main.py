import datetime
import logging

# Configure logging
logging.basicConfig(
    filename='todo_list.log',  # Specify the log file name
    level=logging.INFO,  # Set the log level (you can adjust this as needed)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Define the log message format
)

# Memento Pattern: TaskMemento to store the state of a task.
class TaskMemento:
    """
    TaskMemento stores the state of a task.
    """
    def __init__(self, task):
        self.task = task

# Builder Pattern: TaskBuilder for creating tasks with optional attributes.
class TaskBuilder:
    """
    TaskBuilder class for constructing tasks with optional attributes.
    """
    def __init__(self, description):
        self.task = Task()
        self.task.description = description

    def set_due_date(self, due_date):
        """
        Set the due date for the task.
        :param due_date: A datetime object representing the due date.
        :return: TaskBuilder instance for method chaining.
        """
        self.task.due_date = due_date
        return self

    def set_completed(self, completed):
        """
        Set the completion status of the task.
        :param completed: True if the task is completed, False otherwise.
        :return: TaskBuilder instance for method chaining.
        """
        self.task.completed = completed
        return self

    def build(self):
        """
        Build the Task object.
        :return: Task instance.
        """
        return self.task

# Task class to represent a task with description, due date, and completion status.
class Task:
    """
    Task class represents a task with description, due date, and completion status.
    """
    def __init__(self):
        self.description = ""
        self.due_date = None
        self.completed = False

    def mark_completed(self):
        """
        Mark the task as completed.
        """
        self.completed = True

    def mark_pending(self):
        """
        Mark the task as pending.
        """
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date.strftime('%d-%m-%Y')}" if self.due_date else ""
        return f"{self.description} - {status}{due_date_str}"

# TaskList class to manage tasks.
class TaskList:
    """
    TaskList class manages tasks, including adding, marking completed, and deleting tasks.
    """
    def __init__(self):
        self.tasks = []
        self.undo_stack = []
        self.redo_stack = []

    def add_task(self, task):
        """
        Add a task to the list.
        :param task: Task object to add.
        """
        self.tasks.append(task)
        self.undo_stack.append(TaskMemento(task))
        logging.info(f"Task added: {task.description}")

    def mark_completed(self, description):
        """
        Mark a task as completed by description.
        :param description: Description of the task to mark as completed.
        """
        task = next((t for t in self.tasks if t.description == description), None)
        if task:
            task.mark_completed()
            self.undo_stack.append(TaskMemento(task))
            logging.info(f"Task marked as completed: {task.description}")

    def delete_task(self, description):
        """
        Delete a task by description.
        :param description: Description of the task to delete.
        """
        task = next((t for t in self.tasks if t.description == description), None)
        if task:
            self.tasks.remove(task)
            self.undo_stack.append(None)  # Mark the action as undoable
            logging.info(f"Task deleted: {task.description}")

    def undo(self):
        """
        Undo the last action.
        """
        if self.undo_stack:
            task_memento = self.undo_stack.pop()
            if task_memento:
                self.redo_stack.append(task_memento)
                self.tasks = [t for t in self.tasks if t != task_memento.task]
                logging.info("Undo completed")

    def redo(self):
        """
        Redo the last undone action.
        """
        if self.redo_stack:
            task_memento = self.redo_stack.pop()
            if task_memento:
                self.undo_stack.append(task_memento)
                self.tasks.append(task_memento.task)
                logging.info("Redo completed")

    def get_all_tasks(self):
        """
        Get a list of all tasks.
        :return: List of Task objects.
        """
        return self.tasks

    def get_completed_tasks(self):
        """
        Get a list of completed tasks.
        :return: List of Task objects.
        """
        return [task for task in self.tasks if task.completed]

    def get_pending_tasks(self):
        """
        Get a list of pending tasks.
        :return: List of Task objects.
        """
        return [task for task in self.tasks if not task.completed]

# Helper function to display tasks.
def display_tasks(tasks):
    """
    Display a list of tasks.
    :param tasks: List of Task objects.
    """
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")





if __name__ == "__main__":
    task_list = TaskList()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Mark Completed")
        print("3. Delete Task")
        print("4. Undo")
        print("5. Redo")
        print("6. Show All Tasks")
        print("7. Show Completed Tasks")
        print("8. Show Pending Tasks")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (DD-MM-YYYY, leave blank if none): ")

            try:
                due_date = datetime.datetime.strptime(due_date_str, "%d-%m-%Y") if due_date_str else None
            except ValueError:
                print("Invalid date format. Please enter the date in DD-MM-YYYY format.")
                continue  # Continue the loop to re-enter the date

            task = TaskBuilder(description).set_due_date(due_date).build()
            task_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            description = input("Enter task description to mark as completed: ")
            task = next((t for t in task_list.get_pending_tasks() if t.description == description), None)
            if task:
                task_list.mark_completed(description)
                print("Task marked as completed!")
            else:
                print("Task not found in the pending tasks list.")

        elif choice == "3":
            description = input("Enter task description to delete: ")
            task = next((t for t in task_list.get_all_tasks() if t.description == description), None)
            if task:
                task_list.delete_task(description)
                print("Task deleted!")
            else:
                print("Task not found in the task list.")

        elif choice == "4":
            if task_list.undo_stack:
                task_list.undo()
                print("Undo completed!")
            else:
                print("Nothing to undo.")

        elif choice == "5":
            if task_list.redo_stack:
                task_list.redo()
                print("Redo completed!")
            else:
                print("Nothing to redo.")

        elif choice == "6":
            tasks = task_list.get_all_tasks()
            print("\nAll Tasks:")
            display_tasks(tasks)

        elif choice == "7":
            tasks = task_list.get_completed_tasks()
            print("\nCompleted Tasks:")
            display_tasks(tasks)

        elif choice == "8":
            tasks = task_list.get_pending_tasks()
            print("\nPending Tasks:")
            display_tasks(tasks)

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")
            logging.warning("Invalid choice entered")


