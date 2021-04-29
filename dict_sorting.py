d = {1 : [1,100,1003] , 3: [3,300,1002] , 2:[2,200,1001]}
items = list(d.items())
items.sort(key = lambda x:x[1][2])
print(dict(items))

#Output : 