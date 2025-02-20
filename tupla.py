a=2
b=3
print(f"{a + b = }")

lista = [2, 3, 4]
tupla = (2, 3, 4)
print(f"{tupla[0] =}")

da_tupla_a_lista = list(tupla)
print (f"{da_tupla_a_lista[0] = }")
da_tupla_a_lista[0] = "ciao"
print (f"{da_tupla_a_lista[0] = }")
