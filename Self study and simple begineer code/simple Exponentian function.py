#This is a simple Exponentian function

def power_raise(base_num,pow_num):
    x=1
    for i in range(pow_num):
        x=x*base_num
    return x

a=int(input('Enter base number: '))
b=int(input('Enter power number: '))

print(power_raise(a,b))
