# Exemplo de um programa simples em Python
# Declaração de uma variável nome = "Maria"
# Exibição de uma mensagem na tela

nome = "Maria"
print("olá, " + nome + "! Bem vindo ao mundo da programamação em Python")


# Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")
# Exibe uma mensagem de boas-vindas com o nome do usuário
print("Olá, ", nome, "!Bem-Vindo ao nosso programa!")


# Exibir uma mensagem simples na tela
print("Olá, mundo")

# Exibir o resultado de um cálculo

numero1 = 10
numero2 = 5
soma = numero1 + numero2
print(" A soma dos numeros é:" , soma)

# exibir múltiplos valores separados por virgula

nome = "Maria"

idade = 25
print("Nome:", nome, "| Idade:", idade)


# Calcular a área de um retângulo

largura = 5
altura = 3 
area = largura * altura
print("A área do retângulo é: ", area)

# Encontre o maior entre três números

num1 = 10
num2 = 7
num3 = 12
maior = max(num1,num2, num3)
print("O maior número e: ", maior)


# Cálculo da ára de um circulo

raio = float(input("Digite o raio do circulo:"))
area = 3.14159 * raio**2
print("A área do circulo é:", area)

#Conversão de temperatura de Celsius para Fahrenheit e kelvin

celsius = float(input("Digite a temperatura em celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print("A temperatura em Fahrenheit é: ", fahrenheit)
print("A temperatura em kelvin é: ", kelvin)

# Cálculo do desconto em uma compra
Valor_compra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite o percentual de desconto:"))
valor_desconto = Valor_compra *  desconto / 100
valor_final = Valor_compra - valor_desconto
print("O valor deo desconto é: ", valor_desconto)
print("O valor final da compra com desconto é: ", valor_final)



