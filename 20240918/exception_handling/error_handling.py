def find_q(n,d):
    if d==0:
        raise ZeroDivisionError()
    return n/d

try:
    num=int(input('Enter Numerator:'))
    den=int(input('Enter denominator:'))
    res=find_q(num,den)
    
except ValueError:
    print("Invalid input! Please enter a valid number..")
except ZeroDivisionError:
    print("Denominator cannot be zero!")
else:
    print(res)
finally:
    print("Done!")
print("Program ends here..!")
