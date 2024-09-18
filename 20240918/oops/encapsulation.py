# users=[]
class Account:
    def __init__(self,id,name,age,gender,i_balance=100000):
        self.__id=id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__balance=i_balance
    def __str__(self):
        return f'ID:{self.__id} Name:{self.__name} AGE:{self.__age} GENDER:{self.__gender} Balance:{self.__balance}'
    def credit(self,amount):
        if(amount<0):
            print("Amount is unclear")
            return
        self.__balance+=amount
    def debit(self,amount):
        if(amount>self.__balance):
            print("Insufficient Balance")
            return
        self.__balance-=amount
# def add_record():
#         pass
# def delete_record(id):
#         pass
# def display_by_id(id):
#         pass
# def display_all():
#         pass
# def check_balance(id):
#     for u in users:
# #      if id in users:
#             print(u.balance)

    #endif
#endclass


#menu and driver class

# def menu():
#         choice=int(input('''Please choose one of the options
#                     1.Add a user record
#                     2.Delete an existing patient record by ID
#                     3.Display Record By ID
#                     4.Display All patient records
#                     5.Check balance by ID
#                     6.Credit amount
#                     7.Debit amount
#                     8.Exit'''))
#         if choice == 1:
#             add_record()  
#         elif choice == 2:
#             id=int(input('''Enter Id of the record that you wish to delete:'''))
#             delete_record(id)
#         elif choice == 3:
#             id=int(input('''Enter the ID of patient you wish to display: '''))
#             display_by_id(id)
#         elif choice == 4:
#             display_all()
#         elif choice == 5:
#             id=int(input('''Enter the ID of user to know the balance: '''))
#             check_balance(id)
#         elif choice==6:
#             pass
#         else:
#             print('''Invalid input''')
#         return choice
# #menus
# def menus():
#     choice=menu()
#     while choice!=6:
#         choice=menu()
#     print('''Thanks for using Application!''')
user1=Account(1,'Bhavz',22,'F',900000)
print(user1)
user1.credit(-200000)
print(user1)
user1.debit(1200000)
print(user1.__dict__)


