
class Task:
    def __init__(self, name, description, status="Incomplete"):
        self.name = name
        self.description = description
        self.status = status


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        print(f'Task "{name}" added to the to-do list.')

    def list_tasks(self):
        output = ""
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('Tasks:')
            output+='Tasks:'
            for index, task in enumerate(self.tasks, start=1):
                salidaTask=f'{index}. Name: {task.name}, Description: {task.description}, Status: {task.status}'
                output += salidaTask
                print(salidaTask)
        return output
    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.status = "Complete"
            print(f'Task "{task.name}" marked as complete.')
        else:
            print('Invalid task index.')

    def mark_delayed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.status = "Delayed"
            print(f'Task "{task.name}" marked as delayed.')
        else:
            print('Invalid task index.')

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            print(f'Task "{task.name}" deleted.')
        else:
            print('Invalid task index.')

    def clear_all_tasks(self):
        self.tasks = []
        print('All tasks cleared from the to-do list.')


# Example usage
if __name__ == "__main__":
    todo_manager = ToDoListManager()
    while True:
        print('\nTo-Do List Manager Menu:')
        print('1. Add a new task')
        print('2. List all tasks')
        print('3. Mark a task as completed')
        print('4. Mark a task as delayed')
        print('5. Delete a task')
        print('6. Clear all tasks')
        print('7. Quit')

        choice = input('Enter your choice (1-7): ')

        if choice == '1':
            name = input('Enter task name: ')
            description = input('Enter task description (optional): ')
            todo_manager.add_task(name, description)
        elif choice == '2':
            todo_manager.list_tasks()
        elif choice == '3':
            todo_manager.list_tasks()
            task_index = int(input('Enter the index of the task to mark as completed: '))
            todo_manager.mark_complete(task_index)
        elif choice == '4':
            todo_manager.list_tasks()
            task_index = int(input('Enter the index of the task to mark as delayed: '))
            todo_manager.mark_delayed(task_index)
        elif choice == '5':
            todo_manager.list_tasks()
            task_index = int(input('Enter the index of the task that you want to delete: '))
            todo_manager.delete_task(task_index)
        elif choice == '6':
            todo_manager.clear_all_tasks()
        elif choice == '7':
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')
