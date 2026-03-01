print("Hello World!")
name = ""
while name == "":
    name = input("What is your name? ")
    if name == "":
        pass
    else:
        print(f"Nice to meet you, {name}.")
        