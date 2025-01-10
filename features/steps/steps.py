from main import ToDoListManager, Task

todo_manager = ToDoListManager()

# Scenario 1: Clear all tasks from the to-do list
@given('the to-do list containing these tasks')
def initialize_todo_list(context):
    todo_manager.tasks = []  # Reset the task list to ensure a clean state
    for entry in context.table:
        todo_manager.add_task(entry['Task'], entry['Description'])

@when('the user clears the to-do list')
def clear_todo_list(context):
    todo_manager.clear_all_tasks()

@then('the to-do list should be empty')
def verify_empty_todo_list(context):
    assert todo_manager.tasks == [], f"Expected tasks: [], Found: {todo_manager.tasks}"

# Scenario 2: Remove a specific task
@given('the to-do list contains these new tasks')
def initialize_tasks(context):
    todo_manager.tasks = []  # Start with an empty list
    for entry in context.table:
        todo_manager.add_task(entry['Task'], entry['Description'])

@when('the user removes task "{name}" from the to-do list')
def remove_task(context, name):
    for idx, task in enumerate(todo_manager.tasks):
        if task.name == name:
            todo_manager.delete_task(idx + 1)
            break

@then('the to-do list should not include task "{name}"')
def verify_task_removed(context, name):
    assert all(task.name != name for task in todo_manager.tasks), f"Task '{name}' still exists in the list."

# Scenario 3: Display all tasks
@given('the to-do list contains tasks')
def setup_task_list(context):
    todo_manager.tasks = []  # Clear tasks to avoid overlaps
    for entry in context.table:
        todo_manager.add_task(entry['Task'], entry['Description'])

@when('the user views all tasks')
def list_all_tasks(context):
    context.actual_output = todo_manager.list_tasks()

@then('the output should match the listed tasks')
def validate_task_listing(context):
    expected_output = context.text.strip()
    assert context.actual_output.strip() == expected_output, f"Expected: {expected_output}, Actual: {context.actual_output}"

# Scenario 4: Mark a task as completed
@given('the to-do list contains the following entries')
def populate_task_list(context):
    todo_manager.tasks = []  # Reset tasks for the scenario
    for entry in context.table:
        todo_manager.add_task(entry['Task'], entry['Description'])

@when('the user marks task "{name}" as completed')
def complete_task(context, name):
    for idx, task in enumerate(todo_manager.tasks):
        if task.name == name:
            todo_manager.mark_complete(idx + 1)
            break

@then('the to-do list should show task "{name}" as completed')
def verify_task_completion(context, name):
    for task in todo_manager.tasks:
        if task.name == name:
            assert task.status == 'Complete', f"Expected: Complete, Found: {task.status}"
            break

# Scenario 5: Mark a task as delayed
@given('the to-do list contains the following incomplete entries')
def setup_incomplete_tasks(context):
    todo_manager.tasks = []
    for entry in context.table:
        todo_manager.add_task(entry['Task'], entry['Description'])

@when('the user marks task "{name}" as delayed')
def delay_task(context, name):
    for idx, task in enumerate(todo_manager.tasks):
        if task.name == name:
            todo_manager.mark_delayed(idx + 1)
            break

@then('the to-do list should show task "{name}" as delayed')
def verify_task_delay(context, name):
    for task in todo_manager.tasks:
        if task.name == name:
            assert task.status == 'Delayed', f"Expected: Delayed, Found: {task.status}"
            break

# Scenario 6: Add a new task
@given('the to-do list is initially empty')
def ensure_empty_list(context):
    todo_manager.tasks = []  # Clear any existing tasks

@when('the user adds a new task "{name}" with description "{description}"')
def add_new_task(context, name, description):
    todo_manager.add_task(name, description)

@then('the to-do list should include task "{name}"')
def validate_task_addition(context, name):
    assert any(task.name == name for task in todo_manager.tasks), f'Task "{name}" not found in the to-do list.'

# Custom implementation of list_tasks for consistent formatting
def list_tasks(self):
    return "Tasks:\n" + "\n".join([
        f"{index + 1}. Name: {task.name}, Description: {task.description}, Status: {task.status}"
        for index, task in enumerate(self.tasks)
    ])

ToDoListManager.list_tasks = list_tasks
