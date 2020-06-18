def myfunc(my_string):
    result = ""
    for index, letter in enumerate(list(my_string)):
        if index % 2 == 0:
            result += (letter.lower())
        else:
            result += (letter.upper())

    return result
    # return "".join([letter.lower() if index % 2 == 0 else letter.upper() for index, letter in enumerate(list(myString))])


print(myfunc('hello'))
