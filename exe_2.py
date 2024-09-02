# faça um programa que faça a contagem de ocorrencias de um caracter em uma string

# Funcao que retorna a contagem de ocorrencias do caracter
def contagem_de_ocorrencia(string):
    string = string.lower()
    return string.count('a')

# Input da string
string = str(input("Enter something:  "))

# Imprimindo a contagem de ocorrencias
print(contagem_de_ocorrencia(string))