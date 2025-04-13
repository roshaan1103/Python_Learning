#File Handling

#File name is both are in same folder
#Absolute path if file is in different folder or location
#Types of mode of opening a file:
# 1]r --> read
# 2]w --> write
# 3]a --> append..only add new info at the end of the file
# 4]r+ --> read and write

file=open('filehandling.txt','r') #opens the file
print(file.readable()) #Returns a boolean value if file is readable or not
print('---------------------')
#print(file.read()) #reads th whole file
print('---------------------')

#print(file.readline()) #reads the first line and move to next line
#print(file.readline())
#print(file.readline())
#print(file.readline())
print('---------------------')

#print(file.readlines()[3]) #puts the each line in a list
print('---------------------')

for x in file.readlines():  #Using for loop to print all lines
    print(x)
    
file.close()    #closes the file

#--------------------------------------------------------------

#Writing and appending

#append:

file=open('filehandling.txt','a')

file.write("\nxyz - Finance")

file.close()

#Write:
#this is same as append but if we use write in a pre-existing file it will
#erase all the data
#WE can use write to create a new file
