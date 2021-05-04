def remove_spcl_char(l):
    z = []
    for i in l:
        if i.isalnum():
            z.append(i)
    return z