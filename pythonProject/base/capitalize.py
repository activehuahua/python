import string


def normalize(name):
    return name.capitalize()

L1 = ['adam','LISA','barT']
#L2 = list(map(normalize,L1))
L2 = []
for item in L1:
    L2.append(item.capitalize())
print(L2)