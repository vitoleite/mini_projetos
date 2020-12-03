frutas = "Manga, Banana, Laranja."

print(frutas)

frutas = frutas.upper()
print(frutas)


print(frutas.lower())

"""
Método LOWER - retorna todas as letras em mínusculo
Método UPPER - retorna todas as letras em maíusculo
"""

verduras = "            Batata, Espinafre, Xuxu "

verduras = verduras.strip() # Método strip remove espaços no começo e no fim - também caracteres especiais
print(verduras)


Leites = "aveia, vaca, cabra, amendoas, coco"

lista_leites = Leites.split() # Transforma as palavras em sequencia para listas
print(lista_leites)


Nome = "Joao mora na Rua 2"

localizar = Nome.find("mora") # Busca a variavel e retorna de acordo com a posicao de caracteres
print(Nome[localizar:])

trocar = Nome.replace("Joao", "Maria1.9-") # substitue a variavel por outra de sua escolha
print(trocar)


titulo = 'Em buscA do TeSOuro PerDIDo'.title() # title converte para o formato em titulo.
print(titulo)




sobrenome = "Silva,,, Leite"

novosobrenome = sobrenome.replace(",", ".")

print(novosobrenome)