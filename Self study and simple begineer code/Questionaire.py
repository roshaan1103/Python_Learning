

#inputs:

x=input('Enter your name: ')
y=input('Enter your age: ')

print("Name :" , x )
print("Age :", int(y))

print('-------------------------------')

#Functions with loop:

def compare(c,d):
    i=1
    while i <=3:
        if c > d:
            print(c," is bigger than ",d)
        else :
            print(d," is bigger than ",c)

        i+=1

print("Hello User")
print("Give two number: ")
a=int(input())
b=int(input())

#a1=int(a)
#b1=int(b)

compare(a,b)

print('-----------------------------------------------')

#Dictionaries...to define something with a unique(key) word
#syntax: name={}

cal_month={
        'Jan':'January',
        'Feb':'Feburary',
        'Mar':'March',
        'Apr':'April',
        'May':'May',
        'Jun':'June',
        'Jul':'July',
        'Aug':'August',
        'Sep':'September',
        'Oct':'October',
        'Nov':'November',
        'Dec':'December',
    }

print(cal_month.get('Sep'))

print('-----------------------------------------------')

#For loops:

name=['Roshaan','Ali','Khan']

for i in range(len(name)):
    print(name[i])

print('-----------------------------------------------')

#2D nested listed and printing it using for loop:

num_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
    ]

for row in num_grid:
    for col in row:
        print(col)

print('-----------------------------------------------')
