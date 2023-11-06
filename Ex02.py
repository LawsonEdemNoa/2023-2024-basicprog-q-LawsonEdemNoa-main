import random
# Ex02
def maak_koppels(studenten, aantal_koppels):
    random.shuffle(studenten)#zorgt ervoor dat de lijst als het ware door elkaar geschud wordt
    dict_koppels = {}
    if len(studenten) >= aantal_koppels:
        for i in range(1, aantal_koppels+1):
            dict_koppels[studenten[i]] = studenten[i+1]
            studenten.remove(studenten[i])
    return dict_koppels

print("💘 Koppels binnen Howest 💘")
studenten = ["Karel", "Ben", "Tim", "Ken", "Henk", "Lies", "Barbie", "Sandra", "Debbie"]
aantal_koppels = int(input("Hoeveel koppels moeten er gevormd worden?:> "))
print(maak_koppels(studenten, aantal_koppels))

