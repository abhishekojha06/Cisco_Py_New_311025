class EmployeeManager:

    def __init__(self):
        self.employees = []

    # Convert tuple to dict
    def tuple_to_dict(self, employee_tuple):
        keys = ("id", "name", "job_title", "salary")
        return dict(zip(keys, employee_tuple))

    # Add employee
    def add_employee(self, employee_tuple):
        employee = self.tuple_to_dict(employee_tuple)
        self.employees.append(employee)
        print('Employee Added Successfully')

    # Search employee
    def search_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee["id"] == id:
                return i
        return -1

    # Update employee salary
    def update_employee(self, id, salary):
        index = self.search_employee(id)
        if index != -1:
            self.employees[index]["salary"] = salary
            print('Employee Updated Successfully')
        else:
            print('Employee Not Found.')

    # Delete employee
    def delete_employee(self, id):
        index = self.search_employee(id)
        if index != -1:
            self.employees.pop(index)
            print('Employee Deleted Successfully')
        else:
            print('Employee Not Found')

    # Display all employees
    def display_all(self):
        print("\nAll Employees:")
        for emp in self.employees:
            print(emp)
        print("--------------------------------------")
