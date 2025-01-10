Feature: To-Do List Management

  # Scenario 1: Clear all tasks
  Scenario: Clear the entire to-do list
    Given the to-do list containing these tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
      | Pay bills     | I need to pay the bills |
    When the user clears the to-do list
    Then the to-do list should be empty

  # Scenario 2: Remove a task
  Scenario: Delete a task in the to-do list
    Given the to-do list contains these new tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
      | Pay bills     | I need to pay the bills |
    When the user removes task "Buy groceries" from the to-do list
    Then the to-do list should not include task "Buy groceries"

  # Scenario 3: List all tasks
  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
      | Pay bills     | I need to pay the bills |
    When the user views all tasks
    Then the output should match the listed tasks
      """
      Tasks:
      1. Name: Buy groceries, Description: I need to buy groceries, Status: Incomplete
      2. Name: Pay bills, Description: I need to pay the bills, Status: Incomplete
      """

  # Scenario 4: Mark a task as completed
  Scenario: Mark a task as completed
    Given the to-do list contains the following entries
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  # Scenario 5: Mark a task as delayed
  Scenario: Mark a task as delayed
    Given the to-do list contains the following incomplete entries
      | Task          | Description             |
      | Buy groceries | I need to buy groceries |
    When the user marks task "Buy groceries" as delayed
    Then the to-do list should show task "Buy groceries" as delayed

  # Scenario 6: Add a new task
  Scenario: Adding a task
    Given the to-do list is initially empty
    When the user adds a new task "Buy groceries" with description "I need to buy groceries"
    Then the to-do list should include task "Buy groceries"
