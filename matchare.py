figura = input("Che figura vuoi disegnare?")

match figura:
    case "QUADRATO"| "Q":
        print("Disegno quadrato")
    case "RETTANGOLO" | "R":
        print("Disegno rettangolo")
    case "TRIANGOLO" | "T":
        print("Disegno triangolo")
    case _:
        print("Risposta non valida")