#My first attempt:
for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)


#Another more scalable way:
#Easier to add new conditions & change existing ones
#Credits to Tom Scott
for i in range (1,101):
    output = ""

    if i%3 == 0:
        output += "Fizz"
    if i%5 == 0:
        output += "Buzz"

    if output == "":
        output = i
    
    print(output)


#Or maybe like this?
#Using a dictionary to store all "if condition" pairs
#Can manage all conditions in one place
#Also reduced the repeated use of if statements
for i in range (1,101):
    output = ""

    pairs = {3:"Fizz",
             5:"Buzz",}

    for j in pairs.keys():
        if i%j == 0:
            output += pairs.get(j)
    
    if output == "":
        output = i
    
    print(output)
