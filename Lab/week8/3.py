def long_string(list_of_string):
    x = len(list_of_string[0])
    y = list_of_string[0]
    for i in list_of_string:
        if len(i) > x:
            x = len(i)
            y = i
    return y,x

l = ["cat", "dog", "elephant", "lion", "giraffe"]
z = long_string(l)
print(z)