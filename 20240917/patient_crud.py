patient_record=[]
class Patient:
    def __init__(self, id, name, age, disease, bill):
        self.id=id
        self.name = name
        self.age = age
        self.disease = disease
        self.bill = bill

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Age: {self.age}, Diagnosed with: {self.disease}, Amount paid: {self.bill}'
    
# def add_patient(name,age,disease,bill):
#         pass
# def remove_patient(id):
#         patient_record.remove(id)
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
            id=int(input('''Enter ID:'''))
            name=input('''Enter Name: ''')
            age=int(input('''Enter Age: '''))
            disease=input('''Enter Diaganosed with: ''')
            bill=int(input('''Enter the bill amount paid: '''))
            pt=Patient(id,name,age,disease,bill)
            patient_record.append(pt)
            
        elif choice == 2:
            id=int(input('''Enter Id of the record that you wish to delete:'''))
            for patient in patient_record:
                if patient.id == id:
                    print(patient)
                    if(input("Are you sure you want to delete this record(yes/no):").lower()=='yes'):
                        patient_record.remove(patient)
                        print("Patient record deleted!!!")
                    else:
                        pass
                    return
            print('Patient with given id is not present!!')
        elif choice == 3:
            id=int(input('''Enter the ID of patient you wish to display: '''))
            for pt in patient_record:
                if pt.id == id:
                    print(pt)
                    return
            print("No patient record found by this id!")
        elif choice == 4:
            print('''-----Patient Records-----''')
            for pt in patient_record:
                print(pt)
        elif choice == 5:
            id=int(input('''Enter the ID of patient you wish to update: '''))
            for pt in patient_record:
                if pt.id == id:
                    pt.name=input('''Enter name:''')
                    pt.age=int(input('''Enter Age:'''))
                    return
            print("No patient record found by this id!")
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
#driver program
menus()
