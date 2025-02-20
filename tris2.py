campo = [" "," "," "," ", " ", " ", " ", " "," "]
def stampa_campo():
    print("   A   B    C")
    print(f"1 {campo[0]} | {campo[1]}  |  {campo[2]}")
    print(" ------------")
    print(f"2 {campo[3]} | {campo[4]}  |  {campo[5]}")
    print(" ------------")
    print(f"3 {campo[6]} | {campo[7]}  |  {campo[8]}")


def indice_da_coordinate(coordinata):
    coordinata=coordinata.upper()
    match coordinata:
        case "A1":
            return 0
        case "A2":
            return 1
        case "A3":
            return 2
        case "B1":
            return 3
        case "B2":
            return 4
        case "B3":
            return 5
        case "C1":
            return 6
        case "C2":
            return 7
        case "C3":
            return 8
        case _ :
            return -1
        
def inserisci_valore(coordinata,simbolo):
    if indice_da_coordinate(coordinata) == -1:
        return ("Non valido")
    if campo [indice_da_coordinate(coordinata)] == " ":
        campo[indice_da_coordinate(coordinata)] = simbolo
        return True
    return campo[indice_da_coordinate(coordinata)]

stampa_campo()

