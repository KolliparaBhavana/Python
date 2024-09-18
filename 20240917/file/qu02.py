names_list = input("Enter student names(seperated by spaces): ").split()
names_set = set(names_list)
names_fset = frozenset(names_set)
names_dict = {name:len(name) for name in names_fset}
print(f'Original list: {names_list}')
print(f'Set(No Duplicates): {names_set}')
print(f'Frozen Set: {names_fset}')
print(f'Dictionary of name length: {names_dict}')
import json
with open('qu02.json','w') as names_db:
    json.dump(names_dict,names_db)
print("Dictionary written to JSON file")
with open('qu02.json','r') as names_db:
    names_dict2=json.load(names_db)
    print(f'reading from json file.\n {names_dict2}')
    
   



