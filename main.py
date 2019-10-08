from rot13 import encode, decode
from display import checkUserResponse,encodeSelected, decodeSelected


print("\tBienvenu sur ROT13_scripting !!")
print("Que voulez-vous faire ?\n")
print("[1] - Pour encoder une chaine de caractère")
print("[2] - Pour décoder une chaine de caractère déjà encodé avec ROT13")

cond = True
while cond:
    choice = checkUserResponse(input(">>> "))

    if choice == 1:
        print(encodeSelected())
        cond = False

    elif choice == 2:
        print(decodeSelected())
        cond = False

    else:
        print('Merci de choisir entre 1 ou 2 !!!')
