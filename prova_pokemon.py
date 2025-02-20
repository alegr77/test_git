import requests

def get_pokemon_evolutions(pokemon_name):
    # URL della PokéAPI per ottenere informazioni sulla specie di un Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}/"

    # Fai la richiesta HTTP
    response = requests.get(url)

    # Se la risposta è valida
    if response.status_code == 200:
        data = response.json()

        # Ottieni la URL della catena evolutiva
        evolution_chain_url = data['evolution_chain']['url']
        evolution_response = requests.get(evolution_chain_url)

        if evolution_response.status_code == 200:
            evolution_data = evolution_response.json()
            chain = evolution_data['chain']

            evolutions = []

            # Funzione ricorsiva per esplorare la catena evolutiva
            def explore_chain(chain):
                evolutions.append(chain['species']['name'])
                # Se ci sono evoluzioni successive, esplora anche quelle
                if 'evolves_to' in chain:
                    for evolution in chain['evolves_to']:
                        explore_chain(evolution)

            # Avvia l'esplorazione dalla radice della catena evolutiva
            explore_chain(chain)

            # Restituisci la lista di evoluzioni
            return evolutions
        else:
            return "Errore nel recuperare la catena evolutiva."
    else:
        return "Pokémon non trovato."

# Funzione per chiedere all'utente il nome del Pokémon
def main():
    while True:
        pokemon_name = input("Inserisci il nome del Pokémon (o 'basta' per uscire): ").lower()
        
        if pokemon_name == "basta":
            print("Arrivederci!")
            break
        
        evolutions = get_pokemon_evolutions(pokemon_name)

        if isinstance(evolutions, list):
            if evolutions:
                print(f"Le evoluzioni di {pokemon_name.capitalize()} sono: {', '.join(evolutions)}")
            else:
                print(f"{pokemon_name.capitalize()} non ha evoluzioni.")
        else:
            print(evolutions)

if __name__ == "__main__":
    main()
