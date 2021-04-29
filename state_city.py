a  = ["karnataka","tamilnadu","karnataka","karnataka","tamilnadu","kerala"]
b = ["mysore" ,"chennai" ,  "hassan" , "shivmoga" , "madurai" , "trivendrum" ]
l = list(zip(a,b))
ans  = dict()
a = list(set(a))
for i in a:
	v = []
	for x in l:
		if x[0]==i:
			v.append(x[1])
	ans[i] = v
print(ans)