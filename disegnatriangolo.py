print("Inserisci l'altezza del triangolo")
altezza = int(input())
while altezza <= 1:
    print("Inserisci altezza maggiore di 1")
    altezza = int(input("Inserisci l'altezza del triangolo"))

for contatoreLinea in range (1, altezza+1, 1):
    numeroSpaziDaDisegnare = altezza - contatoreLinea
    for contatoreSpazio in range (1, numeroSpaziDaDisegnare+1,1):
         print(end=" ")
    numeroAsterischiDaDisegnare = 1 + ((contatoreLinea-1)*2)
    for contatoreAsterischi in range (1, numeroAsterischiDaDisegnare+1,1):
        print(end="*")
    print(" ")
    
    #for i in range(altezza):
        #spazi = altezza - i - 1
        #asterischi = i * 2 + 1
        #for j in range(spazi):
            #print(=end"")
        #for j in range (asterischi):
            #print("*", end="")
        #print("")
    #print(f"i: {i} - spazi: {spazi} - asterischi: {asterischi}")
         
    #4s 1a
    #3s 3a
    #2s 5a
    #1s 7a
    #0s 9a