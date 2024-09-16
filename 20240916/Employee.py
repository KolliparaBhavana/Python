class Employee:
    def __init__(self,name,address,code,salary):
        self.name = name
        self.address = address
        self.code = code
        self.salary = salary

    def __str__(self):
        return f'{self.name}, {self.address}, {self.code}, {self.salary}'


Bhavz=Employee('Bhavana', '12-6,Piduguralla', 'BHAVZ1', 1000000)
print(Bhavz)