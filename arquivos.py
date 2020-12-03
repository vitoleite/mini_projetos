arquivo = open('D:\\Users\\vitoo\\Documents\\python\\chaves.txt')

leitura = arquivo.read()
print(leitura)

"""
Função open, abre um arquivo

readlines - lê um arquivo e a quantidade de linhas especificadas
read - lê um arquivo com todas informações
"""

print(open('D:\\Users\\vitoo\\Documents\\python\\chaves.txt').read())

# Para abrir uma pasta em um local diferente, copie o endereço e cole, lembrar de usar duas barras a cada pasta
# colocar o endereço entre uma aspa - Tentar enquadrar todo processo em uma linha.

abrir_arquivo = open('D:\\Users\\vitoo\\Documents\\python\\chaves.txt')

ler = abrir_arquivo.read()

print(ler)