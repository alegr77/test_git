#fibonacci
#0,1,1,2,3,5,8,13
#chiedere all'utente quanti numeri di fibonacci vuol vedere
#stamparli
#quanti numeri di fibonacci vuoi? 5
#0
#1
#1
#2
#3

num_utente = int(input("Quanti numeri della serie di Fibonacci vuoi vedere?"))
num1 = 0
num2 = 1

if num_utente <= 0:
    print("Errore! Inserisci un numero positivo!")
else: 
     for risultato in range(0,num_utente, 1):
          risultato = num1
          num1 = num2
          num2 = risultato + num2
          print(risultato)