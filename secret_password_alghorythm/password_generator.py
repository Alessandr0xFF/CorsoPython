import string
import secrets

def generate_password(
    length: int = 12,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
) -> str:

    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    if avoid_ambiguous: chars += string.ascii_letters

    if avoid_ambiguous:
        for c in "lI1O0":
            chars = chars.replace(c, "")

    return "".join(secrets.choice(chars) for _ in range(length))



def main():
    params = {
        "length": 12,
        "use_upper": True,
        "use_lower": True,
        "use_digits": True,
        "use_symbols": True,
        "avoid_ambiguous": False
    }

    choise = print("[1]Genera password default\n [2]Genera password da scelta")

    if(choise == "1"):
        generate_password()

    elif(choise == "2"):
        params["length"] = int(input("Inserisci lunghezza (es. 16): "))
        params["use_upper"] = get_bool("Includere maiuscole?")
        params["use_lower"] = get_bool("Includere minuscole?")
        params["use_digits"] = get_bool("Includere numeri?")
        params["use_symbols"] = get_bool("Includere simboli?")
        params["avoid_ambiguous"] = get_bool("Evitare caratteri ambigui (l, I, 1, O, 0)?")

        pwd = generate_password(**params)
        print(f"\nPassword generata (personalizzata): {pwd}")

    else:
        print("Scelta non valida.")

if __name__ == "__main__":
    main()