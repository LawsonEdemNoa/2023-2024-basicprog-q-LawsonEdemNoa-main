import random
# Ex03
def selecteer_random_geschenk(dict_wenslijstje_personen):
    for persoon in dict_wenslijstje_personen:
        print(f"{persoon}   -->     {dict_wenslijstje_personen[persoon][random.randint(0, len(dict_wenslijstje_personen[persoon])-1)]}")


# test jouw functie
dict_wenslijstje_personen = {"Stijn":["Fiets","Koptelefoon","Fitbit"], "Marie": ["Game", "Fiets", "Scherm", "Zwemband"], "Joerie": ["Koersfiets", "Zwemband", "Boek"], "Henk":["Laptop","Bak Omer","fiets"]}
print(f"Elke persoon krijgt een willekeurig cadeau van zijn wenslijstje.\nDit is het resultaat:")
selecteer_random_geschenk(dict_wenslijstje_personen)