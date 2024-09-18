console_input=input('''Enter words(seperated by spaces): ''')
list=console_input.split()
t=()
for i in list:
    t+=(i,)
print('''List:''',list)
print('''Tuple:''',t)
with open('lala.txt','w') as fruits:
    fruits.write(f'List: {list}\n')
    fruits.write(f'Tuple: {t}')
print('Data written to file')
print('Reading from file')
with open('lala.txt','r') as fruits:
    fruits_list=fruits.readline()
    fruits_tuple=fruits.readline()
    print(fruits_list+fruits_tuple)
    