import json


def carica_menu(percorso: str) -> dict:
    try:
        with open(percorso, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Errore: Il file '{percorso}' non è stato trovato.")
        return {}
    except json.JSONDecodeError:
        print(f"Errore: Il file '{percorso}' non è un JSON valido.")
        return {}


def piatti_con_allergene(piatti: list, allergene: str) -> list:
    risultato = []
    allergene_low = allergene.lower()
    for piatto in piatti:
        # Estraiamo gli allergeni del piatto e confrontiamoli in minuscolo
        allergeni_piatto = [a.lower() for a in piatto.get("allergeni", [])]
        if allergene_low in allergeni_piatto:
            risultato.append(piatto)
    return risultato


def menu_a_rischio(menu_tipici: list, piatti_per_id: dict, allergene: str) -> list:
    risultato = []
    allergene_low = allergene.lower()

    for menu in menu_tipici:
        piatti_problematici = []
        for id_piatto in menu.get("composizione", []):
            piatto = piatti_per_id.get(id_piatto)
            if piatto:
                allergeni_p = [a.lower() for a in piatto.get("allergeni", [])]
                if allergene_low in allergeni_p:
                    piatti_problematici.append(piatto)

        if piatti_problematici:
            risultato.append((menu, piatti_problematici))
    return risultato


def main():
    data = carica_menu("menu_sakura.json")
    if not data:
        return

    # Estraiamo le liste corrette
    lista_piatti = data.get("piatti", [])
    lista_menu = data.get("menu_tipici", [])

    # Creazione corretta del dizionario di lookup
    piatti_per_id = {piatto["id"]: piatto for piatto in lista_piatti}

    # Input corretto
    allergene_input = input("Inserisci un allergene: ").strip()
    if not allergene_input:
        return

    # Ricerca piatti
    piatti_evitare = piatti_con_allergene(lista_piatti, allergene_input)

    print("\n=== PIATTI DA EVITARE ===")
    if piatti_evitare:
        for piatto in piatti_evitare:
            lista_all_str = ", ".join(piatto['allergeni'])
            print(f"  • {piatto['nome']} ({piatto['categoria']}) — allergeni: {lista_all_str}")
    else:
        print("  Nessun piatto contiene questo allergene.")

    # Ricerca menu - Passiamo piatti_per_id e la stringa allergene_input
    menu_evitare = menu_a_rischio(lista_menu, piatti_per_id, allergene_input)

    print("\n=== MENU TIPICI DA EVITARE ===")
    if menu_evitare:
        for menu, piatti_forbidden in menu_evitare:
            nomi_piatti = ", ".join([p['nome'] for p in piatti_forbidden])
            print(f"  • {menu['nome']} (€{menu['prezzo']:.2f})")
            print(f"      piatti problematici: {nomi_piatti}")
    else:
        print("  Nessun menu contiene questo allergene.")


if __name__ == "__main__":
    main()