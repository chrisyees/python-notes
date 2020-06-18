'''
def myfunc():
    print("Hello World")

def myfunc(name):
    print("Hello " + name)

def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

def myfunc(x, y, z):
    if z:
        return x
    return y

def myfunc(a, b):
    return a + b

def is_even(a):
    return a % 2 == 0

def is_greater(a, b):
    return a > b

def myfunc(*args):
    return sum(args)

def myfunc(*args):
    even_list = []
    for num in args:
        if(num % 2 == 0):
            even_list.append(num)

    return even_list
    #return [num for num in args if num % 2 == 0]
'''


def myfunc(myString):
    result = ""
    for index, letter in enumerate(list(myString)):
        if (index % 2 == 0):
            result += (letter.lower())
        else:
            result += (letter.upper())

    return result
    #return "".join([letter.lower() if index % 2 == 0 else letter.upper() for index, letter in enumerate(list(myString))])

print(myfunc('hello'))