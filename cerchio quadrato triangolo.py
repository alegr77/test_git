import math
print("Di quale figura vuoi calcolare l'area e il perimetro?")
risposta = input()
if risposta == "cerchio":
     print("Hai scelto il cerchio! Qual è il raggio di questo cerchio?")
     raggio = int(input())
     area1 = math.pi * raggio * raggio
     perimetro = math.pi * raggio * 2
     print(f"L'area di questo cerchio è {area1} centimetri quadrati")
     print (f"Il perimetro di questo cerchio è {perimetro} centimetri")

elif risposta == "triangolo":
     print("Hai scelto il triangolo! Vuoi calcolare l'area con base e altezza o col semiperimetro?")
     risposta2 = input()
     if  risposta2 == "semiperimetro":
         print("Inserire i lati del triangolo")
         
         lato1 = int(input())
         lato2 = int(input())
         lato3 = int(input())
         somma1 = lato2 + lato3
         somma2 = lato1 + lato3
         somma3 = lato1 + lato2

         if lato1 < 0 or lato2 < 0 or lato3 < 0:
             print("ERRORE! I lati devono essere positivi")

         if somma1 > lato1 and somma2 > lato2 and somma3 > lato3:
                 perimetro2 = lato1 + lato2 +lato3 
                 print(f"Il perimetro del triangolo è: {perimetro2}")
                 sp = perimetro2 / 2
                 area = math.sqrt(sp * (sp - lato1) * (sp - lato2) * (sp - lato3))
                 print(f"L'area del triangolo è {area}")
         else:
             print("Il triangolo non si può comporre con questi lati")
     else: 
         print("Qual è la base del triangolo?")
         base = int(input())
         print("Qual è l'altezza?")
         altezza = int(input())
         area2 = (base * altezza)/2
         print(f"L'area di questo triangolo è {area2}" , "centimetri quadrati")
           
elif risposta == "quadrato":
     print("Hai scelto il quadrato! Qual è il lato di questo quadrato?")
     lato = int(input())
     area3 = lato * lato
     print(f"L'area di questo quadrato è {area3}" , "centimetri quadrati")

else:
     print("ERRORE!! Figura non riconosciuta!")
