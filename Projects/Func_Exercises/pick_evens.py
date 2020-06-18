def pick_evens(*args):
    even_list = []
    for num in args:
        if(num % 2 == 0):
            even_list.append(num)

    return even_list
    #return [num for num in args if num % 2 == 0]


print(pick_evens(1, 2, 3, 4))
