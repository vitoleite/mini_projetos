# append, len, del, if

lista1 = ["Casa","Carro","Moto","Aviao"]
lista2 = ["Carro", 1, 3.52, True, lista1]

print(lista1)
print(lista2)

print(lista1[1]) # Printando para retornar a variavel 1, que no caso eh Carro
print(lista1[1:4]) #Printando para retornar as variaveis de 1 a 4 - Carro ate Aviao - por que 0 é CASA.

for coisas in lista1:
	print(coisas)

tamanho_lista = len(lista1)
print(tamanho_lista)

lista1.append("Lancha") # Modo append adiciona um item a nossa lista.
print(lista1)

if 5 in lista2:
	print("Contem 5 numeros")

del lista1[2:] # Modo del remove uma variavel da lista, para apagar a lista inteira use: del "lista[:]""
print(lista1)


moto_aquatica = "jetski"

print(moto_aquatica in lista1)	

