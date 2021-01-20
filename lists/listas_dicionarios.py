# pop, min, max, len, sum.
# popitem, update.

number = [3, "cueca", 5]
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2]) # irá retornar o segundo item que no caso é contido num colchete com uma variavel já definida anteriormente (NUMBER) #
print(things[2][2]) # quase a mesma coisa do anterior, só que irá retornar o segundo item da variavel solicitada #

print(things[0])
print(things[0][0:])
print(things[2][1])
print(things[-1]) # retorna inverso, do último ao primeiro.

number.pop(2) # remove um item da lista e o retorna (diferente de del ou remove)
print(number)

print(number+things)

print(len(number)) # conta quantos objetos há numa lista
lista_numeros = [1,2,3,4,5]
print(min(lista_numeros)) # retorna o menor valor da lista, funciona com strings porém a lista deverá ser inteiramente dedicada a string.
print(max(lista_numeros)) # retorna o maior valor da lista, funciona com strings porém a lista deverá ser inteiramente dedicada a string.
print(sum(lista_numeros)) # soma todos valores da lista

loteria = {1: 10, 2: 20, 3: 40, 45: 5, "Cachorro": 748}

loteria.pop(1) # o pop só retorna de acordo com um item proposto, ao que aparenta o pop está excluindo a variavel de acordo com o item.
print(loteria)

loteria.popitem() # só retorna tuplas que estejam definidas "1:10", o popitem retorna o último valor (exclui no caso).
print(loteria)

loteria.update({"Cachorro": 58}) # Aqui alteramos ou incluimos um novo valor
print(loteria)

loteria[6] = "pão de mel" # inserimos um novo valor
print(loteria)

loteria.update({7: "girafa", 8: "danone", 9: "Escada"}) # podemos usar o update para inserir quantos valores quisermos
print(loteria)

loteria.update({10: ("Rato","camundongo","queijo","chumbinho")})
print(loteria)