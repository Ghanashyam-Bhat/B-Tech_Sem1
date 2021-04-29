def my_min(list_int_str):
    
    list_1 = []
    if list_int_str[0].isdigit():
        for i in list_int_str:
            list_1.append(int(i))
    else:
        list_1 = list_int_str
    x = list_1[0]
    for i in list_1:
        if x > i:
            x = i
    return x

z = list(input("Give the input of homogeneous list\n> ").split(","))
a = my_min(z)
print(a)