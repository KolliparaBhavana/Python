def find_Fact(n):
    fact=1
    for i in range(n,1,-1):
        fact=fact*i
    return fact
ans=find_Fact(5)
print(ans)