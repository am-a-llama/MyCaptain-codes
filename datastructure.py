#TASK 1
r= eval(input("Input radius of the circle:  "))
area= 3.1415926535897932*(r**2)
print("The area of the circle wih radius",r,'is:',area)


#TASK 2
fname= input("Input the Filename: ")
for i in range(len(fname)):
    if fname[i]=='.':
        ext= fname[i+1:]
        if ext=='py':
            print('The extension of the file is : "python"')
        elif ext=='doc' or ext=='docx':
            print('The extension of the file is : "MS word"')
        elif ext=='csv':
            print('The extension of the file is : "csv file"')
            
            
            
