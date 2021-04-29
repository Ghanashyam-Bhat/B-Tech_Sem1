#sorting the list in assending order using user defined function
def my_sort(l):
    l_sorted = []
    while len(l)!=0:
        x = l[0]
        for i in l:
            if x > i :
                x = i
        l_sorted.append(x)
        l.remove(x)
    return l_sorted

l = [7,9,5,2,8,7,6]
k = my_sort(l)
print(k)