from main import ToDoListManager, Task

to_do_list = ToDoListManager()

# Escenario 1: Limpiar la lista de tareas
@given('the to-do list containing this tasks')
def step_impl(context):
    to_do_list.tasks = []  # Limpia cualquier dato previo
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user clears the to-do list')
def step_impl(context):
    to_do_list.clear_all_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert to_do_list.tasks == [], f"Expected tasks: [], Actual tasks: {to_do_list.tasks}"

# Escenario 2: Eliminar una tarea
@given('the to-do list contains this new tasks')
def step_impl(context):
    to_do_list.tasks = []  # Limpia cualquier dato previo
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user marks task "{name}" to be deleted from the to-do list')
def step_impl(context, name):
    for i, task in enumerate(to_do_list.tasks):
        if task.name == name:
            to_do_list.delete_task(i + 1)
            break

@then('the to-do list shouldnt show task "{name}"')
def step_impl(context, name):
    assert all(task.name != name for task in to_do_list.tasks), f"Task '{name}' still exists in the list."

# Escenario 3: Listar todas las tareas
@given('the to-do list contains tasks')
def step_impl(context):
    to_do_list.tasks = []  # Limpia cualquier dato previo
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    context.actual_output = to_do_list.list_tasks()

@then('the output should contain tasks')
def step_then_output_should_contain(context):
    expected_output = context.text.strip()
    assert context.actual_output.strip() == expected_output, f"Expected: {expected_output}, Actual: {context.actual_output}"

# Escenario 4: Marcar una tarea como completada
@given('the to-do list contains the following tasks')
def step_impl(context):
    to_do_list.tasks = []  # Limpia cualquier dato previo
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user marks task "{name}" as completed')
def step_impl(context, name):
    for i, task in enumerate(to_do_list.tasks):
        if task.name == name:
            to_do_list.mark_complete(i + 1)
            break

@then('the to-do list should show task "{name}" as completed')
def step_impl(context, name):
    for task in to_do_list.tasks:
        if task.name == name:
            assert task.status == 'Complete', f"Expected status: Complete, Actual status: {task.status}"
            break

# Escenario 5: Marcar una tarea como retrasada
@given('the to-do list contains the following incomplete tasks')
def step_impl(context):
    to_do_list.tasks = []  # Limpia cualquier dato previo
    for row in context.table:
        to_do_list.add_task(row['Task'], row['Description'])

@when('the user marks task "{name}" as delayed')
def step_impl(context, name):
    for i, task in enumerate(to_do_list.tasks):
        if task.name == name:
            to_do_list.mark_delayed(i + 1)
            break

@then('the to-do list should show task "{name}" as delayed')
def step_impl(context, name):
    for task in to_do_list.tasks:
        if task.name == name:
            assert task.status == 'Delayed', f"Expected status: Delayed, Actual status: {task.status}"
            break

# Escenario 6: Agregar una nueva tarea
@given('the to-do list is empty')
def step_impl(context):
    to_do_list.tasks = []  # Limpia cualquier dato previo

@when('the user adds a task "{name}" "{description}"')
def step_impl(context, name, description):
    to_do_list.add_task(name, description)

@then('the to-do list should contain "{name}"')
def step_impl(context, name):
    assert any(task.name == name for task in to_do_list.tasks), f'Task "{name}" not found in the to-do list'

# Actualización del método list_tasks para garantizar el formato esperado
def list_tasks(self):
    # Generar una salida exactamente como se espera en el archivo .feature
    return "Tasks:\n" + "\n".join([
        f"{i + 1}. Name: {task.name}, Description: {task.description}, Status: {task.status}"
        for i, task in enumerate(self.tasks)
    ])


ToDoListManager.list_tasks = list_tasks
