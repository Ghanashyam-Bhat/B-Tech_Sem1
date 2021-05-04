def file_size(file_name):
    z = open(file_name, "r")
    li = z.readlines()
    x = []
    for i in li:
        x.extend(list(i))
    return len(x)+1
