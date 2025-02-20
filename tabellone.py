
def stampa_tabellone(tabellone):

    print(f"\n{tabellone[0]} | {tabellone[1]} | {tabellone[2]}")
    print("--+---+--")
    print(f"{tabellone[3]} | {tabellone[4]} | {tabellone[5]}")
    print("--+---+--")
    print(f"{tabellone[6]} | {tabellone[7]} | {tabellone[8]}\n")


def gioco_tris():

    tabellone = [' '] * 9  

    stampa_tabellone(tabellone)


gioco_tris()
print("  |   |")
print("---------")
print("  |   |")
print("---------")
print("  |   |")