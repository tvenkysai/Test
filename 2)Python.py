//2nd Python Code

class ToDoList:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task: str):
        """Add a new task to the list."""
        if task not in self.tasks:
            self.tasks[task] = False  # False means the task is not completed
        else:
            raise ValueError(f"Task '{task}' already exists.")
    
    def remove_task(self, task: str):
        """Remove a task from the list."""
        if task in self.tasks:
            del self.tasks[task]
        else:
            raise ValueError(f"Task '{task}' does not exist.")
    
    def complete_task(self, task: str):
        """Mark a task as completed."""
        if task in self.tasks:
            self.tasks[task] = True  # True means the task is completed
        else:
            raise ValueError(f"Task '{task}' does not exist.")
    
    def get_tasks(self):
        """Return a list of all tasks."""
        return self.tasks

# Example usage:
# todo_list = ToDoList()
# todo_list.add_task("Buy groceries")
# todo_list.add_task("Clean the house")
# todo_list.complete_task("Buy groceries")
# print(todo_list.get_tasks())



--Unit testing perpose

import unittest

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()
    
    def test_add_task(self):
        self.todo_list.add_task("Task 1")
        self.assertIn("Task 1", self.todo_list.get_tasks())
        self.assertFalse(self.todo_list.get_tasks()["Task 1"])  # Should not be completed

    def test_remove_task(self):
        self.todo_list.add_task("Task 2")
        self.todo_list.remove_task("Task 2")
        self.assertNotIn("Task 2", self.todo_list.get_tasks())
    
    def test_complete_task(self):
        self.todo_list.add_task("Task 3")
        self.todo_list.complete_task("Task 3")
        self.assertTrue(self.todo_list.get_tasks()["Task 3"])  # Should be completed
    
    def test_remove_nonexistent_task(self):
        with self.assertRaises(ValueError):
            self.todo_list.remove_task("Nonexistent Task")
    
    def test_complete_nonexistent_task(self):
        with self.assertRaises(ValueError):
            self.todo_list.complete_task("Nonexistent Task")
    
    def test_add_existing_task(self):
        self.todo_list.add_task("Task 4")
        with self.assertRaises(ValueError):
            self.todo_list.add_task("Task 4")

if __name__ == '__main__':
    unittest.main()
    
    
    
-- --Explanation how I did;
1)ToDoList class:

add_task: Adds a task and sets its status to False (not completed). Raises an error if the task already exists.
remove_task: Removes a task if it exists, otherwise raises an error.
complete_task: Marks a task as completed (True). Raises an error if the task does not exist.
get_tasks: Returns a dictionary with task names as keys and their completion statuses (True/False) as values.

2)Unit Tests:

test_add_task: Verifies adding a task works and that it's initially incomplete.
test_remove_task: Verifies a task can be removed.
test_complete_task: Verifies marking a task as completed works.
test_remove_nonexistent_task: Checks if removing a non-existent task raises an error.
test_complete_nonexistent_task: Ensures that completing a non-existent task raises an error.
test_add_existing_task: Checks that adding a duplicate task raises an error.
