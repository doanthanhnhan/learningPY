# # With NONE
# class Employee:
#   # defining the properties and assigning them none
#   ID = None
#   salary = None
#   department = None

# # Without NONE
# # this code will give a compilation error


# class Employee:
#   # defining the properties and not assigning them none
#   ID
#   salary
#   department

# # Accessing Properties and Assigning Values


# class Employee:
#   # defining the properties and assigning values to them
#   ID = 3789
#   salary = 2500
#   department = "Human Resources"


# # cerating an object of the Employee class
# Steve = Employee()

# # printing properties of Steve - an object of the Employee class
# print("ID =", Steve.ID)
# print("Salary", Steve.salary)
# print("Department:", Steve.department)

# Assigning


class Employee:
  # defining the properties and assigning them None
  ID = None
  salary = None
  department = None


# cerating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
