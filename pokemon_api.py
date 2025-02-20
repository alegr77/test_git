import requests

nome_pokemon = input("Inserisci il nome del pokemon che vuoi cercare: ")
response = requests.get(url=f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")

if response.ok:
    contenuto_risposta = response.json()
    print(f"L'esperienza base di {contenuto_risposta["name"]} è {contenuto_risposta["base_experience"]}")

    print(f"Le abilità di {contenuto_risposta["name"]} sono: ")
    for el in contenuto_risposta["abilities"]:
        print(f"   > {el["ability"]["name"]}")
else:
    print("patatrak!")
    print(response.reason)


