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
    
#menu
def menu():
        choice=int(input('''Please choose one of the options
                     1.Add a patient record
                     2.Delete an existing patient record
                     3.Display patient records
                     4.Exit'''))
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
                    patient_record.remove(patient)
                else:
                    print('Patient with given id is not present!!')
        elif choice == 3:
            print('''-----Patient Records-----''')
            for pt in patient_record:
                print(pt)
            print("Patient records as list")
            print(patient_record)
        elif choice==4:
            pass
        else:
            print('''Invalid input''')
        return choice
#menus
def menus():
    choice=menu()
    while choice!=4:
        choice=menu()
    print('''Thanks for using Application!''')
#driver program
menus()



