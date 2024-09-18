import json
patients=[
        {'ID':1, 'Name': 'bhavana'}, {'Age': 22}, {'Diagnosed with': 'MU'}, {'Amount paid':1000},
        {'ID':1, 'Name': 'bhavana'}, {'Age': 23}, {'Diagnosed with': 'Sk'}, {'Amount paid':1500},
        {'ID':1, 'Name': 'bhavana'}, {'Age': 24}, {'Diagnosed with': 'MU'}, {'Amount paid':2000}
]
patients_str=json.dumps(patients)
print(patients,patients_str)

with open("patients_data.json",'w') as patients_db:
    json.dump(patients,patients_db)

patients_list2=json.loads(patients_str)
print(patients_list2,type(patients_list2))
with open("patients_data.json",'r') as patients_db:
    patients_list3=json.load(patients_db)
    print(patients_list3,type(patients_list3))
    
