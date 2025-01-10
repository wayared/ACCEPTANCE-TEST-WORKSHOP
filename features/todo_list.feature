Feature: To-Do List Management

  # Escenario 1: Limpiar la lista de tareas
  Scenario: Clear the entire to-do list
    Given the to-do list containing this tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
      | Pay bills     | I need to pay the bills |
    When the user clears the to-do list
    Then the to-do list should be empty

  # Escenario 2: Eliminar una tarea
  Scenario: Delete a task in the to-do list
    Given the to-do list contains this new tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
      | Pay bills     | I need to pay the bills |
    When the user marks task "Buy groceries" to be deleted from the to-do list
    Then the to-do list shouldnt show task "Buy groceries"

  # Escenario 3: Listar todas las tareas
  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
      | Pay bills     | I need to pay the bills |
    When the user lists all tasks
    Then the output should contain tasks
      """
      Tasks:
      1. Name: Buy groceries, Description: I need to buy groceries, Status: Incomplete
      2. Name: Pay bills, Description: I need to pay the bills, Status: Incomplete
      """

  # Escenario 4: Marcar una tarea como completada
  Scenario: Mark a task as completed
    Given the to-do list contains the following tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  # Escenario 5: Marcar una tarea como retrasada
  Scenario: Mark a task as delayed
    Given the to-do list contains the following incomplete tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
    When the user marks task "Buy groceries" as delayed
    Then the to-do list should show task "Buy groceries" as delayed

  # Escenario 6: Agregar una nueva tarea
  Scenario: Adding a task
    Given the to-do list is empty
    When the user adds a task "Buy groceries" "I need to buy groceries"
    Then the to-do list should contain "Buy groceries"