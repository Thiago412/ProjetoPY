# def boas_vindas():
#     print('olá marcus')

# boas_vindas()

# def somador(x,y,nome):
#      numero1 = x
#      numero2 = y
#      resultado = numero1 + numero2
#      print(f'{nome} a soma é = {resultado}')


# nome = input('escreva seu nome')
# x = int(input('escolha 1 numero'))
# y = int(input('escolha 1 numero'))


# somador(x,y,nome)

# def boas_vindas(nome, quantidade = 6): #non-default sempre primeiro
#     print(f'olá {nome}')
#     print(f'temos {quantidade} de lapis')

# nome = input('escreva seu nome')
# boas_vindas(nome,4)

# def cliente(nome):
#     return f'olá {nome}'

# print(cliente('Carlos')) # olá carlos
# x = cliente('Andre')
# print(x) # olá andré

#criar uma função que soma vários numeros

# def soma(*numero):
#     somar = 0
#     for i in numero:
#         somar += i
#     return somar


# x = soma(2,3,4,7)
# print(x)

# def agencia(**carro):
#     return carro

# print(agencia(marca = 'Gol',cor = 'Branca',motor = '1.0'))

#Qual o fatorial

import math

print(math.factorial(6))

def fatorial(numero):
    result = 1
    for i in range(numero+1):
        if i != 0:
            result = result * i
        
    return result

numero = int(input('escrava o numero do fatorial:'))
print(fatorial(numero))