
def password_var(given):
    print("""
    The strong password must meet the following conditions :
    1. Atleast eight charecters
    2. Atleast one Uppercase and one Lowercase letter
    3. Atleast one special symbols or a space
    4. Atleast one numerical charecter
    """)
    numbers = "1234567890"
    alph_l = "abcdefghijklmnopqrstuvwxyz"
    alph_h = alph_l.upper()
    spcl_char = r"""`~!@#$%^&*()_-+=|\}{][';":/.,<>? """
    w = 0  # Numerical charecters
    x = 0  # Lowercase alphabet
    y = 0  # Uppercase alphabet
    z = 0  # Special charecter

    for i in given:
        if i in alph_l:
            x += 1
        if i in numbers:
            w += 1
        if i in alph_h:
            y += 1
        if i in spcl_char:
            z += 1
    if len(given) <= 8 or x == 0 or z == 0 or w == 0:
        print("Your password must meet the following conditions to be classfied as strong")
        print("Your password must have:")
    if len(given) < 8:
        print("Lenghth must be atleast 8")
    if x == 0:
        print("Atleast one lowercase charecter")
    if y == 0:
        print("Atleast one uppercase charecter")
    if z == 0:
        print("Atleast one special charecter")
    if w == 0:
        print("Atleast one numerical charecter.")
    if len(given) >= 8 and x != 0 and z != 0 and w != 0:
        print("Your password is strong")
