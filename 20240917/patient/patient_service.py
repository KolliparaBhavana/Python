from patient_entity import patient_record,Patient
def add_patient():
    id=int(input('''Enter ID:'''))
    name=input('''Enter Name: ''')
    age=int(input('''Enter Age: '''))
    disease=input('''Enter Diaganosed with: ''')
    bill=int(input('''Enter the bill amount paid: '''))
    pt=Patient(id,name,age,disease,bill)
    patient_record.append(pt)
def delete_patient(id):
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
def display_by_id(id):
    for pt in patient_record:
        if pt.id == id:
            print(pt)
            return
    print("No patient record found by this id!")
def display_all():
    print('''-----Patient Records-----''')
    for pt in patient_record:
        print(pt)
def update_by_id(id):
    for pt in patient_record:
        if pt.id == id:
            pt.name=input('''Enter name:''')
            pt.age=int(input('''Enter Age:'''))
            return
    print("No patient record found by this id!")
