# inteiros

# ex1
# print("Soma dos números: " + str( int(input("Digite um número inteiro: ")) + int(input("Digite outro número inteiro: "))) )

# ex2
# print("Resto da divisão: " + str(int(input("Digite um número inteiro: ")) % 5 ))

# ex3
# print("Resultado da multiplicação: " + str( (int(input("Digite um número inteiro: "))) * (int(input("Digite outro número inteiro: "))) ))

# ex4
# print("Divisão inteira: " + str( (int(input("Digite um número inteiro: "))) // (int(input("Digite outro número inteiro: "))) ))

# ex5
# print("Quadrado do número: " + str( (int(input("Digite um número inteiro: "))) ** 2 ))

# flutuantes

# ex1
# print("Soma dos números: " + str( float(input("Digite um número flutuante: ")) + float(input("Digite outro número flutuante: ")) ) )

# ex2
# print("Média dos números: " + str( ( float(input("Digite um número flutuante: ")) + float(input("Digite outro número flutuante: ")) ) / 2 ) )

# ex3
# print("Resultado da potência: " + str( (float(input("Digite um número flutuante base: "))) ** (float(input("Digite outro número flutuante expoente: "))) ))

# ex4
# print("Conversão de Celsius para Fahrenheit: " + str( (float(input("Digite a temperatura em Celsius: ")) * 9/5) + 32 ) )

# ex5
# print("Area de um círculo: " + str( 3.14 * (float(input("Digite o raio do círculo: ")) ** 2) ) )

# strings

# ex1
# print("Convertendo para maiúsculas: " + str( input("Digite uma string: ").upper() ) )

# ex2
# print("Nome com as letras minúsculas: " + str( input("Digite seu nome: ").lower() ) )  

# ex3
# print("Resultado com espaços removidos nas extremidades: " + str( input("Digite uma frase: ").strip() ) )

# ex4
# print("imprimindo dia, mês e ano separadamente: " + str( input("Digite uma data no formato DD/MM/AAAA: ").split("/") ) )

# ex5
# print("Concatenando duas strings: " + str( input("Digite a primeira string: ") + " " + input("Digite a segunda string: ") ) )

# booleanos

# ex1
# expr1 = input("Digite a primeira expressão booleana (True/False): ")
# expr2 = input("Digite a segunda expressão booleana (True/False): ")
# resultado = (expr1 == 'True') and (expr2 == 'True')
# print("Resultado da operação AND: " + str(resultado))

# ex2
# expr1 = input("Digite a primeira expressão booleana (True/False): ")
# expr2 = input("Digite a segunda expressão booleana (True/False): ")
# resultado = (expr1 == 'True') or (expr2 == 'True')
# print("Resultado da operação OR: " + str(resultado))

# ex3
# expr = input("Digite uma expressão booleana (True/False): ")
# resultado = not (expr == 'True')
# print("Valor invertido: " + str(resultado))

# ex4
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: ")) 
# sao_iguais = (num1 == num2)
# print("Os números são iguais: " + str(sao_iguais))

# ex5
# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
# sao_diferentes = (num1 != num2)
# print("Os números são diferentes: " + str(sao_diferentes))

# print("Fim dos exercícios da aula II.")

# Exemplo que causa TypeError

# nome = "Alice"

# try:
#     resultado = len(nome)
#     print("O comprimento do nome é:", resultado)
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro

# try:
#     # Código que pode gerar uma exceção
#     resultado = 10 / 0
# except ZeroDivisionError:
#     # Código que executa se a exceção ZeroDivisionError for levantada
#     print("Divisão por zero não é permitida.")

# idade = 20
# if idade < 18:
#     print("Menor de idade")
# elif idade == 18:
#     print("Exatamente 18 anos")
# else:
#     print("Maior de idade")

#Exercício 21: Conversor de Temperatura

# try:
#     celsius = float(input("Digite a temperatura em Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"A temperatura em Fahrenheit é: {fahrenheit}")
# except ValueError:
#     print("Por favor, insira um valor numérico válido para a temperatura.")

#Exercício 22: Verificador de Palíndromo

# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

#Exercício 23: Calculadora Simples

# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     operador = input("Digite o operador (+, -, *, /): ")
#     if operador == '+':
#         resultado = num1 + num2
#     elif operador == '-':
#         resultado = num1 - num2
#     elif operador == '*':
#         resultado = num1 * num2
#     elif operador == '/' and num2 != 0:
#         resultado = num1 / num2
#     else:
#         print("Operador inválido ou divisão por zero.")
#     resultado="NaN"
#     print("Resultado:", resultado)
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")


#Exercício 24: Classificador de Números
# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         print("Positivo")
#     elif numero < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# Exercício 25: Conversão de Tipo com Validação

# entrada_lista = input("Digite uma lista de números separados por vírgula: ")
# numeros_str = entrada_lista.split(",")
# numeros_int = []
# try:
#     for num in numeros_str:
#         numeros_int.append(int(num.strip()))
#     print("Lista de inteiros:", numeros_int)
# except ValueError:
#     print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")

# DESAFIO EXTRA

# Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Verifica se há números no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)

# Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")