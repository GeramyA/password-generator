def einfacher_Zufall(seed, maximum):
    a = 1664525
    c = 1013904223
    m = 2**32

    naechster_Seed = (a * seed + c) % m
    zufallsZahl = naechster_Seed % maximum
    return naechster_Seed, zufallsZahl

def passwort_generieren(laenge):
    zeichen = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "#$%&*+?@!"
    )
    anzahl_zeichen = len(zeichen)
    aktueller_seed = id(object())
    passwort = ""
    for _ in range(laenge):
        aktueller_seed, index = einfacher_Zufall(aktueller_seed, anzahl_zeichen)
        passwort += zeichen[index]

    return passwort


laenge = 16
neues_passwort = passwort_generieren(laenge)
print(f"Generiertes Passwort ({laenge} Zeichen):")
print(neues_passwort)