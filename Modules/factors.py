def factors(a):
    li = []
    while a != 1:
        z = 1
        x = 2
        while z != 0:
            z = a % x
            if z == 0:
                li.append(x)
                a = a//x
            else:
                x += 1
    return li
