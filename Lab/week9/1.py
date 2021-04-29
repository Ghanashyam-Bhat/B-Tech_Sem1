#arrenging the list of dictionaries in the ascending order of the dictionaries
l = [{"name":"Virat", "score":10051,"matches":250}, {"name":"rohit", "score":9051,"matches":180}, {"name":"Sachin", "score":18051,"matches":450}]
l.sort(key="matches")
print(l)