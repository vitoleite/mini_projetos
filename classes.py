# -*- coding: utf-8 -*-
# Class
# Sintaxe

# Marca, Memoria ram, placa de video

class specs_pc: # Cria a classe e dá um especifica um parametro.
	def __init__(self, marca, memoria_ram, placa_de_video): # init será o inicializador do programa
		self.marca = marca
		self.memoria_ram = memoria_ram
		self.placa_de_video = placa_de_video

	def Ligar(self):
		print('1. Turn on')

	def Desligar(self):
		print('2. Turn off')

	def Pc_infos(self):
		print(' '+self.marca+ ',' , self.memoria_ram+ ',' , self.placa_de_video+ '.')


pc1 = specs_pc('Dell','4gb','AMD')
pc2 = specs_pc('Samsung','8gb','Nvidia')
pc3 = specs_pc('Asus','12gb','Intel')

print(pc1.marca,pc1.memoria_ram,pc1.placa_de_video)
print(pc2.marca,pc2.memoria_ram,pc2.placa_de_video)

# Atribuir o self á um parametro é muito útil, pois caso queira utilizar alguma informação, basta vincular o self.

pc4 = specs_pc('Positivo','32gb','RTX')
pc4.Ligar()
pc4.Desligar()
pc4.Pc_infos()


#Classe para Carros.

class Carros:
	def __init__(self,montadora, modelo, ano_lançamento):
		self.montadora = montadora
		self.modelo = modelo
		self.ano_lançamento = ano_lançamento

carro1 = Carros('GM', 'Onix', '2018')
carro2 = Carros('Volkswagen', 'Jetta', '2020')

print(carro1.montadora, carro1.modelo, carro1.ano_lançamento)
print(carro2.montadora, carro2.modelo, carro2.ano_lançamento)