#4.mail
s = 'mohanDas Karamchand gandhi'
l = list(s.split())
ss = l[0][0]+" "+ l[1][0]+" "+l[2]
print(ss.lower())
print(ss.upper())
print(ss.title())
print(s.title())

s = "bad python bad teacher bad lecture"
print(s.replace('bad', 'good')) 
print(s.replace('bad', 'good', 1))
s = "bad python bad teacher bad lecture"
print(s.index('bad'))
print(s.index('bad', s.index('bad') + len('bad')))
i = s.index('bad', s.index('bad') + len('bad'))
print(s[i:].replace('bad', 'worst', 1))
print(s[:i] + s[i:].replace('bad', 'worst', 1))