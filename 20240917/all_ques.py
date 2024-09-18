input_str=input('Enter 5 integers: ').split()
int_list=[int(num) for num in input_str]
int_tuple=tuple(int_list)
int_set=set(int_list)
int_fset = frozenset(int_set)
int_dict = {int:int**2 for int in int_fset}
print(f'Original list: {int_list}')
print(f'Original tuple: {int_tuple}')
print(f'Set(No Duplicates): {int_set}')
print(f'Frozen Set: {int_fset}')
print(f'Dictionary of name length: {int_dict}')

