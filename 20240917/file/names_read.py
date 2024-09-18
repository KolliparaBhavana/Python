#using 'with' clause
""" with open('names.txt','r') as names_db:
    names=names_db.read()
    print(names) """

#without using 'with' clause
""" names_db=open('names.txt','r')
names=names_db.read()
print(names)
names_db.close() """

#using 'with' clause- readlines()
with open('names.txt','r') as names_db:
    names=names_db.readlines()
    print(names)