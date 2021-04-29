#5
str='welcome to engineering at pes university'
s=''
l=str.split(' ')
for i in l:
	i=i[1::]+i[0]
	s=s+' '+i
print(s)

word='hello'
word1=''
for j in word:
	word1=word1+j+'p'
print(word1)
