import requests
from PIL import Image
from io import BytesIO
import os

def get_pokemon_data(pokemon_name):
    """Ottieni i dati di un Pokémon tramite PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore: Pokémon '{pokemon_name}' non trovato!")
        return None

def display_pokemon_image(image_url):
    """Scarica e mostra l'immagine del Pokémon."""
    response = requests.get(image_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.show()
    else:
        print("Errore durante il caricamento dell'immagine!")

def get_pokemon_species_data(pokemon_name):
    """Ottieni i dati della specie di un Pokémon (per evoluzioni) tramite PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Errore: Dati della specie per '{pokemon_name}' non trovati!")
        return None

def get_evolution_chain(evolution_chain_url):
    """Ottieni i dati della catena evolutiva a partire dall'URL della catena."""
    response = requests.get(evolution_chain_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Errore nel recuperare la catena evolutiva!")
        return None

def display_evolution_chain(evolution_chain):
    """Visualizza i nomi dei Pokémon nella catena evolutiva."""
    current_stage = evolution_chain['chain']
    print("\nCatena evolutiva:")
    while current_stage:
        pokemon_name = current_stage['species']['name'].capitalize()
        print(f"- {pokemon_name}")
        next_evolution = current_stage['evolves_to']
        if next_evolution:
            current_stage = next_evolution[0]
        else:
            break

def main():
    while True:
        os.system("CLS")
        print("Benvenuto al gioco Pokémon!")
        pokemon_name = input("Inserisci il nome del Pokémon che vuoi visualizzare: ").strip()

        pokemon_data = get_pokemon_data(pokemon_name)
        if pokemon_data:
            print(f"\nNome: {pokemon_data['name'].capitalize()}")
            print(f"Altezza: {pokemon_data['height'] / 10} m")
            print(f"Peso: {pokemon_data['weight'] / 10} kg")
            print("Statistiche:")
            for stat in pokemon_data['stats']:
                print(f"  - {stat['stat']['name'].capitalize()}: {stat['base_stat']}")

            image_url = pokemon_data['sprites']['front_default']
            if image_url:
                print("\nApro l'immagine del Pokémon...")
                display_pokemon_image(image_url)
            else:
                print("Immagine non disponibile!")

            species_data = get_pokemon_species_data(pokemon_name)
            if species_data and 'evolution_chain' in species_data:
                evolution_chain_data = get_evolution_chain(species_data['evolution_chain']['url'])
                if evolution_chain_data:
                    display_evolution_chain(evolution_chain_data)
            else:
                print("Catena evolutiva non disponibile.")
        else:
            print("Prova con un altro Pokémon.")

        another = input("Vuoi cercare un altro Pokémon? (s/n): ").strip().lower()
        if another != 's':
            print("Programma chiuso")
            break

if __name__ == "__main__":
    main()