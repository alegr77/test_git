print("Vuoi la fanta, il rum o la cocacola?")
bevanda_utente = input()

match bevanda_utente:
    case "fanta":
        print("Vado in cucina a prenderla!")
    case "rum":
        print("Ti verso subito il rum")
    case "cocacola":
        print("Mi spiace ma ho finito la cocacola")
    case _:
        print(f"Non ho capito,non abbiamo {bevanda_utente}")
              