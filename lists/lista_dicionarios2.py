# tuple, zip, list, enumerate

l1 = [1,2,3]
l2 = ("a", "b", "c")

x = zip(l1,l2)
print(tuple(x)) # usamos tuple para ter uma versão melhor compreendida (sem tuple irá retornar só números aleatórios), exemplo abaixo:

print(x)

a1 = [1, 2, 3]
a2 = ["x", "y", "z"]

y = zip(a1,a2)
print(list(y))

b1 = [5, 10, 15]
b2 = ["aa", "cc", "dd", "ee"] 

w = zip(b1,b2)
print(tuple(w)) # A ordem não irá ser alterada, mas os resultados serão limitados conforme a lista.

jota = zip(b1,b2)
print(list(jota))

casa = "linda casa"
casa1 = enumerate(casa)

print(dict(casa1))
# dict conta os espaços, considera-se que junta todos objetos e retornará em uma só variavel. 

casa2 = enumerate(casa)
print(list(casa2)) # diferente de dict, o list separa cada valor por ordem.
