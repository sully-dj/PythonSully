#!/usr/bin/python3
'''
text = "Je dois faire des sauvegarde regulièrements de mes fichiers"
print (text*500)
'''

'''
def exo2():
    pair =[]
    for a in range (0,1000, 2):
        pair.append(a)
        print(pair)
        impair = [n + 1 for n in  pair ]
        print (impair)
exo2()
''''
# exo 3
'''
def table(nb, max=10):
    1 * nb
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1
if __name__ == "__main__":
    table(13)
    '''
# exo4
'''
name = input('Entrez un mot: ')
a = 0
b = 0

while a < len(name):
    if name[a] == 'e':
        b = b + 1
    a = a + 1

print(a)
'''
# exo5
'''
nb = int(input( " entrez un nombre : "))
if nb%2 == 0:
    print("pair")
else:
    print("impair")
    
    ''''''
    # exo6
    ''''''
    nb = int(input(" entrez un nombre : "))
    if (nb < 10):
        print("plus petit ")
    if (nb > 20):
        print ("plus grand ")

    else:
        print  ("oki")
'''
'''
# exo 7  
nbr = (int(input ("Entrez un nombre : "))
 i = 0
 while i <11:
 print ("la suite est : " , nbr + i)
i = i + 1 
'''