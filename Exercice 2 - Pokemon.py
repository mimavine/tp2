import csv

with open("pokemon.csv", "w") as pkm:
    pkm.write("Pikachu,35,55,30,50,40,90 \n")
    pkm.write("Charizard,78,84,78,109,85,100 \n")
    pkm.write("Magikarp,20,10,55,15,20,80 \n")


def charger_pokemons_csv():
    dico = {}
    with open("pokemon.csv", "r") as pokemon:
        stat = csv.reader(pokemon, delimiter=",")
        for row in stat:
            liste_stat = row[1:7]
            liste_stat = [int(i) for i in liste_stat]
            dico[row[0]] = liste_stat
        return dico


pkmn = charger_pokemons_csv()
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
