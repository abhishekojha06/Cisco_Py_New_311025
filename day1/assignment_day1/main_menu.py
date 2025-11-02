from class_to_obj import EmployeeManager

def main():
    manager = EmployeeManager()

    while True:
        print("\n========= Employee Management System =========")
        print("1. Add Employee")
        print("2. Search Employee")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("5. Display All Employees")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
 
        if choice == 1:
              id = int(input("Enter Employee ID: "))
              name = input("Enter Name: ")
              job_title = input("Enter Job Title: ")
              salary = float(input("Enter Salary: "))
              manager.add_employee((id,name, job_title, salary))
        
        elif choice == 2:
             id = int(input("Enter Employee ID to search: "))
             index = manager.search_employee(id)
             if index != -1:
                  print("Employee Found: ", manager.employees[index])
             else:
                  print("Employee Not Found")
        
        elif choice == 3:
             id = int(input("Enter Employee ID to Update: "))
             salary = float(input("Enter New Salary: "))
             manager.update_employee(id, salary)

        elif choice == 3:
             id = int(input("Enter Employee ID to update: "))
             salary = float(input("Enter the salary: "))
             manager.update_employee(id, salary)
        
        elif choice == 4:
            id = int(input("Enter Employee ID to Delete: "))
            manager.delete_employee(id)

        elif choice == 5:
            manager.display_all()

        elif choice == 6:
            print("👋 Exiting Program...")
            break

        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()