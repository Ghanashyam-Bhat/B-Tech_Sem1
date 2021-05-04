def listinput():
    l=[]
    n=int(input('Enter the number of inputs you want in the list:'))
    i=0
    f=1
    while i<n:
        print('Enter the element number', f )
        k=input('')
        l.append(k)
        i=i+1
        f=f+1
    return l

