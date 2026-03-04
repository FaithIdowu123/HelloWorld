#Prints hello world
print("Hello World!")

#Variable that stores user name as a string
name = ""

#Code that prevents the program from moving forward unless a name is given
while name == "":
    #Gets the name from the user as a string
    name = input("What is your name? ")

    #Restarts the loop if no name is given
    if name == "":
        pass
    else:
        #Prints a message with the user's name 
        print(f"Nice to meet you, {name}.")
        