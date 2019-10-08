from rot13 import encode, decode


def checkUserResponse(choice):
    userChoice = 0
    try:
        userChoice = int(choice)
        return userChoice
    except ValueError:
        print("Merci d'entré un chiffre !!!")
        checkUserResponse(input(">>> "))


def encodeSelected():
    print("\nInscrivez le mot ou la phrase à encoder :\n")
    return encode(input('>>> '))


def decodeSelected():
    print("\nInscrivez le mot ou la phrase à décoder :\n")
    return decode(input('>>> '))
