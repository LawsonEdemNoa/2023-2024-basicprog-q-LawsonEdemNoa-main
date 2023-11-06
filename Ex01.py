# Ex01
def calculate_love_score(eerste_naam, tweede_naam):
    list_gem_letters = []
    aantal_gem_letters = 0
    for i in eerste_naam:
        if i in tweede_naam:
            list_gem_letters.append(i)
            aantal_gem_letters += 1
    return f"Gemeenschappelijke letters: {list_gem_letters}\nAantal Gemeenschappelijke letters: {aantal_gem_letters}\nGemiddelde lengte van de namen: {(len(eerste_naam)+len(tweede_naam))/2}\nScore: {round((aantal_gem_letters/((len(eerste_naam)+len(tweede_naam))/2))*100, 1)}"
    # returnt alle gemeennschappelijke letters, aantal gemeennschappelijke letters, Gemiddelde lengte van de namen berekend door de som van de lengte van de namen te delen door 2 en de score wat de afgeronde waarde is van de Gemiddelde lengte van de namen gedeeld door aantal gemiddelde letters maal 100
eerste_naam = input("Geef een eerste naam op:> ")
tweede_naam = input("Geef een tweede naam op:> ")
print(calculate_love_score(eerste_naam, tweede_naam))
