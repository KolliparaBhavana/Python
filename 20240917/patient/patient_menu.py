from patient_entity import patient_record,Patient
from patient_service import add_patient,delete_patient,display_by_id,display_all,update_by_id
#menu
def menu():
        choice=int(input('''Please choose one of the options
                    1.Add a patient record
                    2.Delete an existing patient record by ID
                    3.Display Record By ID
                    4.Display All patient records
                    5.Update Record By ID
                    6.Exit'''))
        if choice == 1:
            add_patient()  
        elif choice == 2:
            id=int(input('''Enter Id of the record that you wish to delete:'''))
            delete_patient(id)
        elif choice == 3:
            id=int(input('''Enter the ID of patient you wish to display: '''))
            display_by_id(id)
        elif choice == 4:
            display_all()
        elif choice == 5:
            id=int(input('''Enter the ID of patient you wish to update: '''))
            update_by_id(id)
        elif choice==6:
            pass
        else:
            print('''Invalid input''')
        return choice
#menus
def menus():
    choice=menu()
    while choice!=6:
        choice=menu()
    print('''Thanks for using Application!''')