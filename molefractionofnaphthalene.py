massofnaphthalene=float(input("enter mass of naphthalene"))
massofbiphenyl=float(input("enter mass of naphthalene"))

nn=0.0
nb=0.0
nn=massofnaphthalene/128
nb=massofbiphenyl/154
totmoles=nn+nb
molefractionofnaphthalene=nn/totmoles
print("the mole fraction of naphthalene=",molefractionofnaphthalene)
