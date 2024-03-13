import pandas as pd
import os.path
from os import path


#Custom Exception
class unable_to_access(Exception): 
    def __init__(self):
       self.message = "Unable to retrieve employee data, please try again"
    def __str__(self):
        print(self.message)
        return self.message


#Menu
def menu():
    print("****************************************")
    print("*     Employee Menu                    *")
    print('* 1. Add new employee                  *')
    print('* 2. Update Employee Information       *')
    print('* 3. Remove Employee                   *')
    print('* 4. List Employee Information         *')
    print('* 5. Exit                              *')
    print("*                                      *")
    print("****************************************")

#sample data
def reset_data():
    employee_dict =  {'First Name': ['Brandon', 'Mike', 'Jose', 'Chris', 'Nicole'],
                    'Last Name': ['Boyd', 'Einziger', 'Pasillas', 'Kilmore', 'Row'],  
                    'Employee_ID': [1, 2, 3, 4, 5], 
                    'Date of Employment': ['1991', '1991', '1991', '1998', '2023'], 
                    'Salary': [1000000, 900000, 800000, 700000, 600000], 
                    'Department': ['Vocals', 'Lead Guitar', 'Drums', 'Turntable', 'Bass']}
    employee_df = pd.DataFrame(employee_dict)
    employee_df.to_csv('Employees.csv', index=False)

#add new employee
def add_new_employee():
    if (path.isfile('Employees.csv')):
        data = pd.read_csv('Employees.csv')
        emp_first_name = input("What is the new employee's first name?")
        emp_last_name = input("What is the new employee's last name?")
        emp_ID = len(data.Employee_ID) + 1
        date_of_employ = input("When was the new employee hired?")
        emp_salary = input("What is the new employee's salary?")
        emp_dept = input('Which department was the new employee hired for?')
        df2 = pd.DataFrame({'First Name': [emp_first_name], 'Last Name': [emp_last_name], 'Employee_ID': [emp_ID], 'Date of Employment': [date_of_employ], 'Salary': [emp_salary], 'Department': [emp_dept]})        
        data = pd.concat([data,df2], ignore_index = True)
        data.to_csv('Employees.csv', index=False)
    else:
        reset_data()
        raise(unable_to_access)

#update employee
def update_employee(): 
    if (path.isfile('Employees.csv')):
        emp_id = input('What is the employee ID?')
        print("Available fields are: First Name, Last Name, Date of Employment, Salary.")
        update_field = str(input('Which field do you want to update?'))
        new_value = input('What should the new value be?')
        index = int(emp_id) -1
        data = pd.read_csv('Employees.csv')
        data.at[index, update_field] = new_value
        data.to_csv('Employees.csv', index=False)
    else:
        reset_data()
        raise(unable_to_access)

#remove employee
def remove_employee():
    if (path.isfile('Employees.csv')):
        emp_id = input('What is the employee ID?')
        index = int(emp_id)- 1
        data = pd.read_csv('Employees.csv')
        data = data.drop(index)
        data.to_csv('Employees.csv', index=False)
    else:
        reset_data()
        raise(unable_to_access)

#list all employees
def employee_list():
    data = pd.read_csv('Employees.csv')
    print(data)



    


#If used in a new environment, uncomment this line
#reset_data()
i = 0


while i!=5:
    menu()
    i = int(input())

    if i in (1, 2, 3, 4, 5):
        if i==1:
            add_new_employee()
            
            continue
        elif i==2:
            update_employee()
            
            continue
        elif i==3:
            remove_employee()
            
            continue
        elif i==4:
            employee_list()
            
            continue
        elif i==5:
            break

