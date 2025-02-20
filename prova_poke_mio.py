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

def display_evolution_chain(evolution_chain, displayed_pokemon):
    """Visualizza le immagini delle evoluzioni shiny, evitando duplicati."""
    current_stage = evolution_chain['chain']
    evolution_order = []  # Lista per tenere traccia dell'ordine delle evoluzioni
    
    while current_stage:
        pokemon_name = current_stage['species']['name'].lower()
        evolution_order.append(pokemon_name)
        
        # Passa all'evoluzione successiva, se presente
        next_evolution = current_stage['evolves_to']
        if next_evolution:
            current_stage = next_evolution[0]
        else:
            break

    # Ora visualizza le evoluzioni in ordine
    print("\nCatena evolutiva (con immagini shiny):")
    for pokemon_name in evolution_order:
        # Verifica se l'immagine del Pokémon è già stata mostrata
        if pokemon_name not in displayed_pokemon:
            # Ottieni i dati del Pokémon nella catena evolutiva per l'immagine shiny
            evolution_data = get_pokemon_data(pokemon_name)
            if evolution_data:
                # Controlla la versione shiny e mostra l'immagine se disponibile
                shiny_url = evolution_data['sprites'].get('front_shiny')
                if shiny_url:
                    print(f"  - Mostro l'immagine shiny di {pokemon_name.capitalize()}...")
                    display_pokemon_image(shiny_url)
                    displayed_pokemon.add(pokemon_name)  # Aggiungi il Pokémon all'elenco dei già mostrati
                else:
                    print(f"  - Nessuna versione shiny disponibile per {pokemon_name.capitalize()}.")

def display_pokemon_types(pokemon_data):
    """Mostra i tipi del Pokémon."""
    print("Tipi:")
    for t in pokemon_data['types']:
        print(f"  - {t['type']['name'].capitalize()}")

def check_shiny_version(pokemon_data):
    """Controlla se esiste una versione shiny e stampa il risultato."""
    shiny_url = pokemon_data['sprites'].get('front_shiny')
    if shiny_url:
        print("\nEsiste una versione shiny del Pokémon! Mostrerò l'immagine shiny.")
        return True
    else:
        print("\nNessuna versione shiny disponibile per questo Pokémon.")
        return False

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

            # Visualizza i tipi del Pokémon
            display_pokemon_types(pokemon_data)

            # Controlla e mostra l'immagine shiny del Pokémon
            if check_shiny_version(pokemon_data):
                shiny_url = pokemon_data['sprites']['front_shiny']
                if shiny_url:
                    display_pokemon_image(shiny_url)

            # Ottieni i dati della specie per la catena evolutiva
            species_data = get_pokemon_species_data(pokemon_name)
            if species_data and 'evolution_chain' in species_data:
                evolution_chain_data = get_evolution_chain(species_data['evolution_chain']['url'])
                if evolution_chain_data:
                    # Aggiungi il Pokémon principale all'elenco di quelli già mostrati
                    displayed_pokemon = {pokemon_name.lower()}
                    display_evolution_chain(evolution_chain_data, displayed_pokemon)
            else:
                print("Catena evolutiva non disponibile.")
        else:
            print("Prova con un altro Pokémon.")

        # Cambiamo la logica per accettare "S", "s", "SI", "si"
        another = input("Vuoi cercare un altro Pokémon? (s/n): ").strip().lower()
        if another in ['s', 'si']:
            continue
        else:
            print("Programma chiuso")
            break

if __name__ == "__main__":
    main()




   
