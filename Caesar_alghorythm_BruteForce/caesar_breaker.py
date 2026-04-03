def caesar(message) -> str:
    result = ""
    lista = []

    for index in range(26):
        for char in message:
            if 'A' <= char <= 'Z':
                ascii_offset = 65
                new_char = chr((ord(char) - ascii_offset - index) % 26 + ascii_offset)
                result += new_char

        lista.append((index, result))
        result = ""


    return lista



def main():
    text_to_convert =input("\nInserisci il testo da decifrare").strip().upper()
    result = caesar(text_to_convert)
    print(f"\nTesto Decifrato: {result}")


if __name__ == "__main__":
    main()