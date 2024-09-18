""" def find_diff(n1:int=2,n2:int=4)->int:
    return n1-n2
print(find_diff(10,20))
print(find_diff(n2=20,n1=10))
print(find_diff(20,10))
print(find_diff(n2=10))
print(find_diff())#-2

def change_name(names,index,name):
    names[index]=name
names=['rahul','modi']
print(names)
change_name(names,1,'bhavz')
print(names)

print(sum([10,20,30,40,50]))

#argument others here is used as variable argument
def find_sum(first,second,*others):
    #print(type(others))
    s=first+second
    if(len(others)>0):
        for n in others:
            s+=n
        #end for
    #end if
    return s
print(find_sum(10,20))
print(find_sum(10,20,30,40))
print(find_sum(10,20,30,50,60))

#argument others here is used as variable named argument
def find_sum(first,second,**others):
    print(type(others))
    s=first+second
    if(len(others)>0):
        for key in others:
            s+=others[key]
        #end for
    #end if
    return s
print(find_sum(first=10,second=20,t=3))
print(find_sum(first=10,second=20,t=30,f=40))
print(find_sum(first=10,second=20,t=30,f=50,fi=60)) """

#recursive function
""" def fact(N):
    if N<=1:
        return 1
    #end-if
    return N * fact(N-1)
print(fact(5)) """

#debugger
import math
def is_prime(n):
    n_sqrt=int(math.sqrt(n))
    for i in range(2,n_sqrt+1):
        if(n%i==0):
            return False
        #end-if
    #end-for
    return True

print(is_prime(61))
print(is_prime(93))
print(is_prime(8))
