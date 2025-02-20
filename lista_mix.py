#data una lista variegata di numeri e stringhe 
#tenere solamente i numeri e stamparli in ordine decrescente (usando anche la funzione lambda)

lista_mista = ["ciao", 77, 18, "lato", -2, 5, "ordine", 4.5] 


numeri_lista =list(filter(lambda numero : numero != int, lista_mista))
print(numeri_lista)

numeri = list(filter(lambda numero: isinstance(numero, (int, float)), lista_mista))
print(numeri)

numeri.sort(reverse=True)
print(numeri)

