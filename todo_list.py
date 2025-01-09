class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if not task.strip():
            raise ValueError("Task cannot be empty.")
        self.tasks.append({"task": task, "completed": False})

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                return
        raise ValueError(f"Task '{task}' not found.")

    def clear_tasks(self):
        self.tasks = []

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                return
        raise ValueError(f"Task '{task}' not found.")

# Example usage (can be removed in production)
if __name__ == "__main__":
    todo = ToDoListManager()
    todo.add_task("Buy groceries")
    todo.add_task("Pay bills")
    print("Tasks:", todo.list_tasks())
    todo.mark_task_completed("Buy groceries")
    print("After completing a task:", todo.list_tasks())
    todo.remove_task("Pay bills")
    print("After removing a task:", todo.list_tasks())
    todo.clear_tasks()
    print("After clearing tasks:", todo.list_tasks())
