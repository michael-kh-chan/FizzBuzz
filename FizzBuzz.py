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