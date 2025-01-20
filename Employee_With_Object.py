#Question 2:  Create a Python module named employee that contains a class
# Employee with attributes  name, salary and methods get_name() and get_salary().

#Write a program to use this module to create an object of the Employee class
# and display its name and salary.

import Employee_data

emp = Employee_data.Employee("Rejith Joseph", 50000)
print("Employee Name: ", emp.get_name())
print("Employee Salary: ", emp.get_salary())

emp = Employee_data.Employee("Maria Michael", 45000)
print("Employee Name: ", emp.get_name())
print("Employee Salary: ", emp.get_salary())