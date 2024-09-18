from functools import reduce
nums=[10,20,30]
sum_nums=reduce(lambda x,y:x+y,nums,0)
prod_nums=reduce(lambda x,y:x*y,nums,1)
print(sum_nums)
print(prod_nums)

nums=[2,4,7]
square_nums=list(map(lambda x:x**2,nums))
print(square_nums)

nums_even=list(filter(lambda x:x%2==0,nums))
print(nums_even)


nums_min=reduce(lambda x,y:min(x,y),nums)
print(nums_min)

nums_max=reduce(lambda x,y:max(x,y),nums)
print(nums_max)

#another way to do it:
nums_minn=reduce(min,nums)
nums_maxx=reduce(max,nums)
print(nums_minn,nums_maxx)