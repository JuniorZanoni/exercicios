import math

# Exercicio 1 - Crie uma função que receba dois números e retorne o maior deles.
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


# Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
def media_arimetica(lista):
    soma_lista = 0
    for numero in lista:
        soma_lista += numero
    return soma_lista / len(lista)


# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n
def quadrado_de_asteriscos(valor):
    if valor > 1:
        for numero in range(valor):
            print('*' * valor)
    else:
        print('O valor deve ser maior que 1')    


# Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres
def maior_nome(lista):
    maior_nome = ''
    for nome in lista:
        if len(nome) > len(maior_nome):
            maior_nome = nome
    return maior_nome


#Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede(em m²).
def orcamento(metros_quadrados):
    LATA_GRANDE = {
        "litros": 18,
        "preco": 80,
        "cobertura_por_litro": 3,
    }
    latas = metros_quadrados / (LATA_GRANDE['cobertura_por_litro'] * LATA_GRANDE['litros'])
    return (math.ceil(latas), (math.ceil(latas) * LATA_GRANDE['preco']))


# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo
def tipo_de_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        print('Triângulo Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo Isósceles')
    elif lado1 != lado2 != lado3:
        print('Triângulo Escaleno')
    else:
        print('Não é um triângulo')

# Bonûs - exercício 1: Dada uma lista, descubra o menor elemento. Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2.
def menor_elemento(lista):
    menor_numero = lista[0]
    for numero in lista:
        if numero < menor_numero:
            menor_numero = numero
    print(menor_numero)


# Bonûs - exercício 2: Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um triângulo retângulo com n asteriscos de base. Por exemplo, para n = 5 o triângulo terá 5 asteriscos na base:
def triangulo_asterisco(numero):
    for numero in range(1, numero + 1):
        print('*' * numero)


# Bonûs - exercício 3: Crie uma função que receba um número inteiro N e retorne o somatório de todos os números de 1 até N. Por exemplo, para N = 5, o valor esperado será 15.
def soma_todos_numeros(numero):
    print(sum(range(1, numero + 1)))


# Bonûs - Exercício 4: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#  Álcool:
# Até 20 litros, desconto de 3% por litro;
# Acima de 20 litros, desconto de 5% por litro.
#
# Gasolina:
# Até 20 litros, desconto de 4% por litro;
# Acima de 20 litros, desconto de 6% por litro.
#
# Escreva uma função que receba o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A - álcool, G - gasolina), e retorne o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 2,50, e o preço do litro do álcool é R$ 1,90.
def desconto_combustivel(litros, tipo):
    if tipo == 'A':
        if litros > 20:
            return (litros * 1.9) * 0.5
        else:
            return (litros * 1.9) * 0.3
    else:
        if litros > 20:
            return (litros * 2.5) * 0.6
        else:
            return (litros * 2.5) * 0.4
