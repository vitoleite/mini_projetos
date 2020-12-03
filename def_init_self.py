# -*- coding: utf-8 -*-

class Chat:
	def __init__(self, nome):
		self.nome = nome

	def fala(self):
		print('olá, '+self.nome+'!')

a = Chat('Vitor')
a.fala()

b = Chat('Juscelino')
b.fala()

c = Chat('Tudo bem')
c.fala()

print(b.nome)        # o  B está linkado como uma variavel de self #


"""
__init__ é útil para fazer qualquer inicialização que você queira com seu objeto. 
Ele é o método "Inicializador" da instancia. Na primeira inicialização temos o self como primeiro parametro e logo após
Temos o parametro nome.

Sendo que o self.nome é um novo campo que retorna o parametro NOME
"""