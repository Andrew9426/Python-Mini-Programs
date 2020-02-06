'''Scrieti un program ce va numara cate caractere are un sir de caractere dat
de utilizator. Aceasta numarare sa se realizeze cu ajutorul unui for fara a utiliza
len(). La final afisati rezultatul.'''


sir = input("Introdu un sir de caractere: ")

numar = sum(1 for x in sir)
print(numar)

