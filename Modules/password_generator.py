# Password Generator
def password_gen():
    numbers = "1234567890"
    alph_l = "abcdefghijklmnopqrstuvwxyz"
    alph_h = alph_l.upper()
    spcl_char = r"""`~!@#$%^&*()_-+=|\}{][';":/.,<>? """
    import random

    u_l = list(alph_h)*3
    l_l = list(alph_l)*3
    n_l = list(numbers)*3
    s_l = list(spcl_char)*3
    lists = u_l + l_l + n_l + s_l
    q = random.randint(8, 12)
    w = 0  # Numerical charecters
    x = 0  # Lowercase alphabet
    y = 0  # Uppercase alphabet
    z = 0  # Special charecter
    n = 0
    while n == 0:
        t = random.sample(lists, q)
        for i in t:
            if i in alph_l:
                x += 1
            elif i in numbers:
                w += 1
            elif i in alph_h:
                y += 1
            elif i in spcl_char:
                z += 1
        if x != 0 and y != 0 and z != 0 and w != 0:
            generated = ""
            n += 1
            for k in t:
                generated += k
            print(f"Your password is \n{generated}")
