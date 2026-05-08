# Inicializace seznamu úkolů
ukoly = []

def zobrazit_ukoly():
    """Zobrazí všechny úkoly v seznamu."""
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
    else:
        print("\nSeznam úkolů:")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

def pridat_ukol():
    """Umožní uživateli přidat nový úkol s názvem a popisem."""
    while True:
        nazev = input("\nZadejte název úkolu: ").strip()
        if not nazev:
            print("Chyba: Název úkolu nesmí být prázdný!")
            continue
        
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print("Chyba: Popis úkolu nesmí být prázdný!")
            continue
            
        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

def odstranit_ukol():
    """Zobrazí úkoly a umožní uživateli jeden odstranit podle čísla."""
    zobrazit_ukoly()
    if not ukoly:
        return

    try:
        cislo = int(input("\nZadejte číslo úkolu, který chcete odstranit: "))
        if 1 <= cislo <= len(ukoly):
            odstraneny = ukoly.pop(cislo - 1)
            print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        else:
            print("Chyba: Úkol s tímto číslem neexistuje.")
    except ValueError:
        print("Chyba: Prosím zadejte platné číslo.")

def hlavni_menu():
    """Hlavní ovládací smyčka programu."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost (1-4): ")

        if volba == '1':
            pridat_ukol()
        elif volba == '2':
            zobrazit_ukoly()
        elif volba == '3':
            odstranit_ukol()
        elif volba == '4':
            print("\nKonec programu.")
            break
        else:
            print("\nNeplatná volba, zkuste to znovu.")

# Spuštění programu
if __name__ == "__main__":
    hlavni_menu()
