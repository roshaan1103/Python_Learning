# Try / Except block method for error handling

try:
    number= int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Invalid Input")
#Types of error:
#1) ZeroDivisionError
#2) Value Error
