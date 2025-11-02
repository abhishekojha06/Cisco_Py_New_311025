employees = []

#Convert tuple to dict
def tuple_to_dict(employee_tuple):
    keys = ("id", "name", "job_title", "salary")
    return dict(zip(keys, employee_tuple))

#Adding Employee
def add_employee(employee_tuple):
    employee = tuple_to_dict(employee_tuple)
    employees.append(employee)
    print('Employee Added Successfully')

def search_employee(id):
    for i, employee in enumerate(employees):
        if employee["id"] == id:
            return i
    return -1

def update_employee(id, salary):
    index = search_employee(id)
    if index != -1:
        employees[index]["salary"] = salary
        print('Employee Updated Successfully')
    else:
        print('Eployee Not Found. ')

def delete_employee(id):
    index = search_employee(id)
    if index != -1:
        employees.pop(index)
        print('Employee Deleted Successfully')
    else: 
        print('Employee Not Found')


#Adding Employee
add_employee((101,'Pratik', 'Software Engineer', 56000))
add_employee((102,'Abhishek', 'Software Automation Engineer', 40000))
add_employee((103,'Rishabh', 'Software Automation Engineer', 99000))
add_employee((104,'Nihar', 'Software Automation Engineer', 99))
add_employee((105,'Divya', 'Business Analyst', 45000))


print(employees)

print("======================================================")

#search employee

emp_index = search_employee(104)
if emp_index != -1:
    print('Searched emloyee:', employees[emp_index])
else:
    print('Employee Not Found.')


print("========================================================")

#update salary
update_employee(104, 99200)
print(employees)

print("=========================================================")


#Add and delete and employee
add_employee((106, 'Raj', 'Python Trainer', 4200))
print(employees)

print("=========================================================")


#delete employee
delete_employee(106)
print(employees)
