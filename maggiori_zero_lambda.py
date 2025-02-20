lista_numeri = [-2, 6, 7, 9, -1]
def maggiori_zero(numero):
    return numero > 0
for i in lista_numeri:
    print(maggiori_zero(numero[i]))

lista_maggiori_zero = list(filter(lambda numero : numero > 0, lista_numeri))
print(lista_maggiori_zero)

lista_maggiori_zero = list(filter( maggiori_zero, lista_numeri))
print(lista_maggiori_zero)

#aggiungiConLambda = lambda x, y : x+y
#aggiungiConLambda(5,3)
#print(aggiungiConLambda(5,3))