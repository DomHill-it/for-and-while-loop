#For Loop by Dominique Hill

#Prompt the user for a starting number
starting_number=eval(input("Enter a start number"))

#Prompt the user for a stopping number
stopping_number=eval(input("Enter a stop number"))

#Prompt the user for a stepping number
stepping_number=eval(input("Enter a step number"))

#For Loop
for x in range (starting_number, stopping_number, stepping_number):
    print(x)