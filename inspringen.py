import random

def raad_het_getal():
    willekeurig_getal = random.randint(1, 100)
    aantal_pogingen =0

    while True:
        gok = int(input("Raad het getal tussen 1 en 100: "))
        aantal_pogingen += 1

        if gok == willekeurig_getal:
            print(f"Goed zo je hebt het getal binnen {aantal_pogingen} beurten geraden.")
           
        elif gok < willekeurig_getal:
            print("Te laag! Probeer het opnieuw.")
        else:
            print("Te hoog! Probeer het opnieuw.")

raad_het_getal()
