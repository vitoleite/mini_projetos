# -*- coding: utf-8- -*-
a = "Bolo"
b = "de"
c = "laranja"

Junção = a + " " + b + " " + c
print(Junção)

# função LEN serve para contar caracteres ou palavras.

tamanho = len(Junção)
print(tamanho)

lista1 = ["Maçã","Banana","Laranja"]

qtd = len(lista1)
print(qtd)

print(a[0])
print(a[1])
print(a[2])
print(a[3])


print(Junção[0:7])
print(Junção[0:]) # Aqui a junção no caso como não se limitou a uma quantidade de caracteres, ela retorna do primeiro ao infinito


""" No primeiro caso contamos a quantidade de letras obtidas a partir da soma de A + B + C (isso juntamente com os espaços somados na operação)
- Segundo, contamos a quantidade de palavras na lista.
- Terceiro foi somente a contagem de uma string (Bolo) a partir das letras, 0 = primeira letra B, 1 = segunda O ...
- Quarto a partir de um determinado número a outro.
"""
