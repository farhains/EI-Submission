# EI-Submission
console based to do list using python
# To-Do List Manager with Python

This Python program is a To-Do List Manager that allows users to manage tasks with descriptions, due dates, and completion statuses. It employs design patterns such as the Memento Pattern and Builder Pattern to create a robust and extensible task management system.

## Features

- **Add Task**: Users can add tasks to the list, including optional attributes like due dates.

- **Mark Completed**: Tasks can be marked as completed, changing their status from pending to completed.

- **Delete Task**: Users can delete tasks from the list.

- **Undo and Redo**: The program supports undo and redo functionality, allowing users to reverse or replay their actions.

- **View Tasks**: Users can view all tasks, completed tasks, and pending tasks separately.

## Design Patterns

This program showcases the use of two design patterns:

1. **Memento Pattern**: The `TaskMemento` class is used to store the state of a task. This is particularly helpful for implementing undo and redo functionality.

2. **Builder Pattern**: The `TaskBuilder` class is responsible for creating tasks with optional attributes. It allows for easy and flexible task creation.

In brief, your To-Do List Manager code demonstrates adherence to SOLID principles and OOP concepts as follows:

## SOLID Principles

1. **Single Responsibility Principle (SRP)**:
   - Each class has a single, well-defined responsibility, making the code maintainable.

2. **Open/Closed Principle (OCP)**:
   - The code is open for extension (new features) without modifying existing code.

3. **Liskov Substitution Principle (LSP)**:
   - While not explicitly using inheritance, the code allows for easy extension and specialization.

4. **Interface Segregation Principle (ISP)**:
   - Classes provide focused and minimal sets of methods related to their responsibilities.

5. **Dependency Inversion Principle (DIP)**:
   - Classes depend on abstractions, promoting flexibility in component swapping.

## OOP Concepts

1. **Encapsulation**:
   - State and behavior of tasks are encapsulated within the `Task` class, hidden from external access.

2. **Abstraction**:
   - Abstract representations of tasks and mementos are created, allowing high-level manipulation.

3. **Inheritance** (implicitly):
   - The code is designed for future use of inheritance when extending functionality.

4. **Polymorphism**:
   - Tasks are interacted with in a generic way, supporting flexibility in task handling.

5. **Modularity**:
   - Code is organized into separate classes, enhancing readability and maintainability.

6. **Composition**:
   - Complex objects (e.g., task lists) are composed from simpler components (e.g., tasks).

These principles and concepts contribute to a well-structured and extensible codebase, allowing for future enhancements and modifications while maintaining code integrity and readability.

## Usage

1. **Adding a Task**: To add a task, select option 1, enter the task description, and, optionally, provide a due date in DD-MM-YYYY format.

2. **Marking a Task as Completed**: Choose option 2 and enter the task description to mark it as completed.

3. **Deleting a Task**: Select option 3 and enter the task description to delete it.

4. **Undo and Redo**: Options 4 and 5 allow you to undo and redo actions, respectively.

5. **Viewing Tasks**: Options 6, 7, and 8 let you view all tasks, completed tasks, and pending tasks.

6. **Exiting the Program**: Choose option 9 to exit the program.

## Logging

The program uses a logging system to record actions and errors. Logs are written to a file named `todo_list.log` in the same directory as the script.

## Error Handling

The program provides some basic error handling, including validation for date format input and checks for invalid choices.

## Dependencies

- Python 3.x

## Getting Started

1. Download the Python script (`todo_list.py`) to your local machine.

2. Make sure you have Python 3.x installed.

3. Run the script in your terminal or command prompt.

## Example

Here's an example of how to use the To-Do List Manager:

```
To-Do List Manager
1. Add Task
2. Mark Completed
3. Delete Task
4. Undo
5. Redo
6. Show All Tasks
7. Show Completed Tasks
8. Show Pending Tasks
9. Exit

Enter your choice: 1
Enter task description: Buy groceries
Enter due date (DD-MM-YYYY, leave blank if none): 15-10-2023
Task added successfully!

... (continue using the program)

```

## Feedback and Contributions

This To-Do List Manager is open-source and can be improved or extended. Feel free to provide feedback or contribute to its development.

Please report any issues or suggest enhancements by opening an issue on the GitHub repository: [Link to GitHub Repository](https://github.com/your-github-repo)

## License

This To-Do List Manager is licensed under the [MIT License](LICENSE).

---

Enjoy using the To-Do List Manager!
