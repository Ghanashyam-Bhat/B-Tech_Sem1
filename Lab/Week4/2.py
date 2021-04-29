li = ["500", "50","zebra", "pes", "Univesity56", "+-*oo8", "an"]
l_d = []
l_s = []
l_n = []
l_sp = []
# A)
for i in li:
    if not i.isalnum():
        l_sp.append(i)
    elif i.isdigit():
        l_n.append(i)
    elif i.isalpha():
        l_s.append(i)
    elif i.isalnum():
        l_d.append(i)
print(l_s, l_n, l_sp, l_d)
# B)
l_d.sort()
l_n.sort()
l_sp.sort()
l_s = sorted(l_s)
print(l_s, l_n, l_sp, l_d)