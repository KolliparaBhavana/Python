from patient_entity import Patient
patient_record=dict()
def add_patient(id):
    
    name=input('''Enter Name: ''')
    age=int(input('''Enter Age: '''))
    disease=input('''Enter Diaganosed with: ''')
    bill=int(input('''Enter the bill amount paid: '''))
    pt=Patient(id,name,age,disease,bill)
    patient_record[pt.id]=pt
def delete_patient(id):
        pt=patient_record.get(id)
        if  pt == None:
            print("No patient record found by this id! {id}")
            return
        if(input("Are you sure you want to delete this record(yes/no):").lower()=='yes'):
            del patient_record[id]
            print("Patient record deleted!!!")
def display_by_id(id):
    pt=patient_record.get(id)
    if pt == None:
        print("No patient record found by this id! {id}")
        return
    print(pt)

def display_all():
    print('''-----Patient Records-----''')
    for id in patient_record:
        print(patient_record[id])
def update_by_id(id):
    pt=patient_record.get(id)
    if pt==None:
        print("No patient record found by this id!")
        return
    pt.name=input('''Enter name:''')
    pt.age=int(input('''Enter Age:'''))
    print("Patient details updated:)")
    print(pt)
    
