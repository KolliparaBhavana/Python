salaries=[10,12,14,16,18,20]
def add_salary(salary):
    global salaries
    salaries.append(salary)
    print(salaries)
def delete_salary(salary):
    global salaries
    if salary in salaries:
        salaries.remove(salary)
        print(salaries)
    else:
        print("Sorry given salary is not listed")
def find_avg():
    global salaries
    avg=0
    n=len(salaries)
    for i in salaries:
        avg=avg+i
    avg=avg/n
    print('Average of salaries is ',avg)
def find_sum():
    global salaries
    sum=0
    for i in salaries:
        sum=sum+i
    print('Sum of salaries is ',sum)
def find_min():
    global salaries
    min=salaries[0]
    for i in salaries:
        if min>i:
            min=i
    # min=min(salaries)
    print("Minimum salary present is ",min)

def find_max():
    global salaries
    max=salaries[0]
    for i in salaries:
        if max<i:
            max=i
    print("Maximum salary present is ",max)

def menu():
    global salaries
    choice=int(input('''Please choose one of the options
                     1.Add a salary
                     2.Delete an existing salary
                     3.Find Average
                     4.Find Sum
                     5.Find Minimum
                     6.Find Maximum
                     7.Exit'''))
    if choice == 1:
        salary=int(input('''Enter Salary:'''))
        add_salary(salary)
    elif choice == 2:
        salary=int(input('''Enter Salary that you wish to delete:'''))
        delete_salary(salary)
    elif choice == 3:
        find_avg()
    elif choice == 4:
        find_sum()
    elif choice == 5:
       find_min()
    elif choice == 6:
        find_max()
    else:
        print('''Application Ended!''')

def menus():
    choice=menu()
    while choice !=8:
        choice=menu()



menus()
    