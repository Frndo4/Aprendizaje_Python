print("Escribe alguna letra: ")
letra=str(input())

def if_is_vowel():
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'u':
        return True
    elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'U':
        return True
    else:
        return False

print(if_is_vowel())
