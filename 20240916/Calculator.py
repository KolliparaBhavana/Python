def find_calc(first:int,second:int)->int:
        sum=first + second
        diff=first - second
        prod = first *second
        quotient=first // second
        return sum,diff,prod,quotient

s,d,p,q=find_calc(20,6)
print(s,d,p,q)
tup=find_calc(10,2)
print(tup)