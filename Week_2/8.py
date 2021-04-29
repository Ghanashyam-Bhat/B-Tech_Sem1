#Bench problem
# a,b,c are the number of students in each class respectively
a = 20
b = 21
c = 22
print(f"Number of students in class a={a} , b={b}, c={c}")
# at, bt, ct are minimum number of benches required for each class
at = a//2+a%2
bt = b//2+b%2
ct = c//2+c%2
print(f"Numaber of bench required for a={at} , b= {bt} , c={ct}")
print(f"Total number of benches required are {at+bt+ct}")