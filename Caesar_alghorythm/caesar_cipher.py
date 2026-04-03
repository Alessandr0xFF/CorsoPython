
def encrypt(message, key) -> str:
    result = ""
    for char in message:
#65-90
        if 'A' <= char <= 'Z':
            ascii_offset = 65
            new_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += new_char

#97-122
        elif 'a' <= char <= 'z':
            ascii_offset = 97
            new_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += new_char
        else:
            result += char

    return result


def main():
    print(f"CIFRARIO DI CESARE")
    choice = int(input("[1]Cifrare, [2]Decifrare\n"))

    if choice not in [1, 2]:
        print("invalid choice")
        return

    message = input("Inserisci il contenuto da cifrare/decifrare\n").strip().upper()
    try:
        key = int(input("Inserisci chiave\n"))
    except ValueError:
            print("Errore: La chiave deve essere un numero intero.\n")
            return

    if choice == 1:
        result = caesar(message, key)
        print(f"\nTesto Cifrato: {result}")
    elif choice == 2:
        result = caesar(message, -key) #passo il negativo della chiave
        print(f"\nTesto Decifrato: {result}")

if __name__ == "__main__":
    main()

