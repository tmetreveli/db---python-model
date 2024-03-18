# Employee Database Management System

## Overview

This Python module provides a simple interface for managing employee records in a database. Utilizing SQLite as its database back-end, it offers functionalities to create, read, update, delete, and list employee records through an easy-to-use Employee class.

## Features

- Get Employee: Retrieve an employee record by its primary key.
- Create Employee: Add a new employee record to the database.
- Update Employee: Update existing employee details.
- Delete Employee: Remove an employee record from the database.
- List Employees: Fetch a list of employee records based on specified criteria.
- Save Changes: Persist changes to an employee record, whether it's an update or a new creation.
- Comparing Employees: Compare two employees based on their age.

## Requirements

- Python 3.x
- SQLite3
  
## Getting Started

Database Setup: Ensure you have an SQLite database set up and a table for the employees created. The expected table name is employee with columns for id, name, surname, and age. The id column should be set as the Primary Key (PK).

# Module Import:
Before using the Employee class, import the database cursor c from your database connection module:
```
  from db import c
```
# Creating an Employee Instance:
```
  new_employee = Employee(name="John", surname="Doe", age=30)
```
# Saving the Employee Record to the Database:
```
  new_employee.save()
```
# Fetching an Employee Record:
```
existing_employee = Employee.get(pk=1)
if existing_employee is not None:
    print(existing_employee)
```
# Updating an Employee Record:
  ```
  existing_employee.name = "Jane"
  existing_employee.save()
```
# Deleting an Employee Record:
  ```
    existing_employee.delete()
```
# Listing Employees Based on Criteria:
```
employees = Employee.get_list(name="John")
for emp in employees:
    print(emp)
```
