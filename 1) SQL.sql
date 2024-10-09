
--1st Question Answer
--first we need to create a Employee table
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    department VARCHAR(255),
    salary DECIMAL(10, 2),
    hire_date DATE
);

-- I inserted some values in employee table

INSERT INTO employees (name, department, salary, hire_date)
VALUES 
('John Doe', 'Sales', 55000.00, '2022-01-15'),
('Jane Smith', 'Marketing', 62000.00, '2021-07-23'),
('Robert Johnson', 'Sales', 53000.00, '2020-11-01');

--Retrieve all employees in a specific department (e.g., Sales):

SELECT * FROM employees
WHERE department = 'Sales';

--Update the salary of a specific employee (e.g., employee with ID 3):

UPDATE employees SET salary = 56000.00 WHERE id = 3;

--Delete an employee record by ID (e.g., employee with ID 4):

DELETE FROM employees WHERE id = 4;

--Retrieve the average salary of employees in each department:

SELECT department, AVG(salary) AS average_salary
FROM employees GROUP BY department;

-- Retrieve a list of all employees along with their department names (from the employees and departments tables):

CREATE TABLE departments ( id INT PRIMARY KEY, department_name VARCHAR(255) );

--If an employee does not belong to a department, their department name should show as NULL.

SELECT e.name, e.department, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department = d.department_name;


