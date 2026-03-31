# class Employee:
#     def __init__(self, name, emp_id):
#         self.name = name
#         self.emp_id = emp_id
#     def display_employee(self):
#         print(f"Employee Name: {self.name}, ID: {self.emp_id}")
# class Department:
#     def __init__(self, dept_name):
#         self.dept_name = dept_name
#     def display_department(self):
#         print(f"Department: {self.dept_name}")
# class Manager(Employee, Department):
#     def __init__(self, name, emp_id, dept_name):
#         Employee.__init__(self, name, emp_id)  # Initialize Employee
#         Department.__init__(self, dept_name)    # Initialize Department
#     def display_manager(self):
#         self.display_employee()  
#         self.display_department()  
# manager = Manager("Alice", 101, "HR")   
# manager.display_manager()
