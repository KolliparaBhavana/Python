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