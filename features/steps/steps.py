from behave import given, when, then
from todo_list import ToDoListManager

# Initialize the To-Do List Manager
to_do_list_manager = ToDoListManager()

@given('the to-do list is empty')
def step_impl(context):
    to_do_list_manager.clear_tasks()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    to_do_list_manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = [t["task"] for t in to_do_list_manager.list_tasks()]
    assert task in tasks, f'Task "{task}" not found in the to-do list.'

@given('the to-do list contains tasks:')
def step_impl(context):
    to_do_list_manager.clear_tasks()
    for row in context.table:
        to_do_list_manager.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.listed_tasks = to_do_list_manager.list_tasks()

@then('the output should contain:')
def step_impl(context):
    listed_tasks = [t['task'] for t in context.listed_tasks]
    for row in context.table:
        assert row['Task'] in listed_tasks, f'Task "{row["Task"]}" not found in the output.'

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    to_do_list_manager.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    tasks = to_do_list_manager.list_tasks()
    for t in tasks:
        if t["task"] == task:
            assert t["completed"] is True, f'Task "{task}" is not marked as completed.'
            return
    raise AssertionError(f'Task "{task}" not found in the to-do list.')

@when('the user clears the to-do list')
def step_impl(context):
    to_do_list_manager.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(to_do_list_manager.list_tasks()) == 0, "The to-do list is not empty."

@when('the user tries to add an empty task')
def step_impl(context):
    try:
        to_do_list_manager.add_task("")
    except ValueError as e:
        context.error_message = str(e)

@then('the system should display an error "{error_message}"')
def step_impl(context, error_message):
    assert context.error_message == error_message, f'Expected error message: "{error_message}", but got: "{context.error_message}".'

@when('the user removes the task "{task}"')
def step_impl(context, task):
    to_do_list_manager.remove_task(task)

@then('the to-do list should contain only:')
def step_impl(context):
    remaining_tasks = [t['task'] for t in to_do_list_manager.list_tasks()]
    for row in context.table:
        assert row['Task'] in remaining_tasks, f'Task "{row["Task"]}" is missing in the to-do list.'
    assert len(remaining_tasks) == len(context.table), "The to-do list contains extra tasks."
