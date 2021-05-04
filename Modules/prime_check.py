def is_it_prime(x):
    z = 0
    if x % 2 == 0:
        y = x//2
    else :
        y = (x+1)//2
    for i in range(2, y):
        if x % i == 0:
            z += 1
    if z == 0:
        print("Prime")
    elif z != 0:
        print("Not prime")