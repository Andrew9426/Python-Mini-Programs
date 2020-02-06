'''Creati un program ce are ca scop sortarea a x elemente introduse de
utilizator de la tastatura printr-o bucla while. Elementele vor fi inserate pe rand
intr-o lista prin acest while de catre utilizator prin capturare de text. De
asemenea utilizatorul are datoria sa insereze la inceputul programului cate
elemente doreste sa insereze in lista. Trebuie sa afisam lista la final.'''

lista = []
nr = input("Cate elemente doresti sa inserezi in lista? :")
while len(lista) < int(nr):
    lista.append(input())
print("Lista ta este :", lista)
