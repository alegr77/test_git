import requests
import os
while True:
    nome = input("Inserisci nome primo pokemon: ")
    nome2 = input("Inserisci nome secondo pokemon: ")

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}/")
    response2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome2}/")

    if response.ok and response2.ok:
        rispostajson = response.json()
        rispostajson2 = response2.json()
        break
    else:
        continue

#######confronto statistiche#######
os.system("cls")
input_nome = input("Su quale statistica vuoi fare il confronto? ")
os.system("cls")

for i in range(len(rispostajson["stats"])):
    if input_nome != "tutti" and input_nome == rispostajson["stats"][i]["stat"]["name"]:
        if rispostajson["stats"][i]["base_stat"] >= rispostajson2["stats"][i]["base_stat"]:
            stat_pkmn1 = rispostajson["stats"][i]["base_stat"]
            stat_pkmn2 = rispostajson2["stats"][i]["base_stat"]
            print(f"{nome.capitalize():<15} {nome2.capitalize():>20}")
        else:
            stat_pkmn1 = rispostajson2["stats"][i]["base_stat"]
            stat_pkmn2 = rispostajson["stats"][i]["base_stat"]
            print(f"{nome2.capitalize():<15} {nome.capitalize():>20}")
        nome_stat = rispostajson["stats"][i]["stat"]["name"]
        print(f"{stat_pkmn1:<10}{nome_stat:^15}{stat_pkmn2:>10}")
        break

    elif input_nome == "tutti":
        stat_pkmn1 = rispostajson["stats"][i]["base_stat"]
        stat_pkmn2 = rispostajson2["stats"][i]["base_stat"]
        nome_stat = rispostajson["stats"][i]["stat"]["name"]
        print(f"{stat_pkmn1:<10}{nome_stat:^15}{stat_pkmn2:>10}")