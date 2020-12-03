# -*- coding: utf-8 -*-

print("Seja bem-vindo, para começar, digite seu nome.")

lista_nomes = ["Vitor", "Suzane", "Cauan", "Paloma"]

nome = input('>: ')

if nome in lista_nomes:
	print("\nSério que você está tentando este código novamente?")

print("\nMuito bem, "+ nome+', '+ "agora precisamos da sua idade.")

idade = input('>:')

print("Okay, vimos aqui que você tem: "+ idade+ " anos de idade, "+"esperamos que seja verdade!")

print("\nDiga-nos aonde tu moras:")

local = input('>: ')

print("\nUau, "+ local+ " é um belo lugar :D")

print("\nCerto, chega de papo. Para sabermos o seu IMC, precisamos de seu peso e altura")

valor_peso = float(input('Insira seu peso: '))

print ("\nAVISO - Para a sua altura digite da seguinte forma: 1.55")

valor_altura = float(input('\nAgora insira sua altura: '))

valor_imc = valor_peso / (valor_altura*valor_altura)

print(f'\nSeu IMC é: {valor_imc:.2f}')

if valor_imc < 18.5:
	print("\nA classificação do seu IMC está como Magreza")
elif valor_imc < 24.9:
	print("\nA classificação do seu IMC está como Normal")
elif valor_imc < 29.9:
	print("\nA classificação do seu IMC está como Sobrepeso")
elif valor_imc < 39.9:
	print("\nA classificação do seu IMC está como Obesidade")
else:
	print("\nA classificação do seu IMC está como Obesidade Grave, cuidado.")

""" Para limitar as casas decimais utilizei o F strings, que substitue o .format"""

input()
