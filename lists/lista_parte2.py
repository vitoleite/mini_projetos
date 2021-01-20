lista = [15,5,6,8,1,0,4,3,85,259,2452]

lista.sort() # funcao sort, ordena as variaveis de uma lista
print(lista)

lista.sort(reverse=True) # funcao sort com reverse, nesse caso ordenou por ordem decrescente.
print(lista)

lista.reverse() # reverte a lista.
print(lista)


lista.remove(0) # remove uma variavel da lista
print(lista)

for excluir in lista:
	if excluir == 5:
		lista.remove(excluir)

print(lista)