# Funcao que retorna a sequencia de fibonacci
def fibonacci_sequency(num):
    sequency_numbers = [0,1]
    while True:
        next_value = sequency_numbers[-1] + sequency_numbers[-1] # Soma penultimo e último valor da sequencia de fibonacci
        if next_value > num:
            print("Valor do número da sequencia é maior do que o valor de parâmetro")
            break
        sequency_numbers.append(next_value) # Adicionado o novo valor a lista
        return sequency_numbers # Retornando a lista de fibonacci
    
# Funcao que verifica se o valor de input está presente na sequencia de fibonacci
def is_fibonacci_in_sequency(num):
    fibonacci_numbers = fibonacci_sequency(num) # Aqui pega a sequencia gerada pela primeira funcao
    return num in fibonacci_numbers # Aqui faz uma verificacao se o valor de input está presente na lista, tendo um valor de output do tipo booleano (True or False)

# Definindo o número a ser verificado
num = int(input("Enter with the number: "))

# Verificando se o número pertence à sequência de Fibonacci
if is_fibonacci_in_sequency(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")