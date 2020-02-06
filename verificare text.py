text = input("Introuceti textul : ")


numar = "Sirul de caractere este format din numere"
litere = "Sirul de caractere este format din litere"
altceva = "Sirul de caractere este format din diferite elemente"

if text.isdigit():
    print(numar.center(80))
elif text.isalpha():
    print(litere.swapcase())
else:
    print(altceva.join("#!"))