Feature: To-Do List Management

    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"

    Scenario: List all tasks in the to-do list
        Given the to-do list contains tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user lists all tasks
        Then the output should contain:
            | Task          |
            | Buy groceries |
            | Pay bills     |

    Scenario: Mark a task as completed
        Given the to-do list contains tasks:
            | Task          | Status  |
            | Buy groceries | Pending |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed

    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user clears the to-do list
        Then the to-do list should be empty

    Scenario: Prevent adding an empty task
        Given the to-do list is empty
        When the user tries to add an empty task
        Then the system should display an error "Task cannot be empty."

    Scenario: Remove a specific task
        Given the to-do list contains tasks:
            | Task          |
            | Buy groceries |
            | Pay bills     |
        When the user removes the task "Pay bills"
        Then the to-do list should contain only:
            | Task          |
            | Buy groceries |
