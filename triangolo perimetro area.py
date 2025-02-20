import math  

print("Inserisci il primo lato del triangolo")
lato1 = int(input())
print("Inserisci il secondo lato del triangolo")
lato2 = int(input())
print("Inserisci il terzo lato del triangolo")
lato3 = int(input())
perimetro = lato1 + lato2 + lato3

if lato1 + lato2 > lato3 and lato1 + lato3 > lato2 and lato2 + lato3 > lato1:
    print(f"Il perimetro del triangolo è: {perimetro}")

    sp = perimetro / 2
    area = math.sqrt(sp * (sp - lato1) * (sp - lato2) * (sp - lato3))
    print(f"L'area del triangolo è {area}")
else:
    print("ERRORE! Non è un triangolo!")