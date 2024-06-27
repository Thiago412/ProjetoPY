# t = 3
# x = str(3)
# y = int(4)
# z = float(5)

# print(t)
# print(t+t)
# print(x+x)
# print(y+y)
# print(z+z)

'''
O Andre tem 32 anos e mora em São Paulo
'''

################## prints
# nome = 'Andre'
# nome = input('qual o seu nome :')
# idade = 32 #ou idade = str(idade)
# estado = 'São Paulo'

# print('o ' + nome + ' tem '+ str(idade) + ' e mora em ' + estado)

# ano_nascimento = input('em que ano vc nasceu?')
# idade = 2020 -int(ano_nascimento)
# print(idade)

# fruta = 'abacate'
# print(fruta[2:6]) #acat
# print(fruta[-1])  #e
# valor = str(99.75)
# print(valor[3:5]) #75

# nome = 'Marcus'
# sobrenome = 'Silva'
# profissao = 'programador'

# texto = f'o {nome} {sobrenome} é {profissao}'
# print(texto) #o Marcus Silva é programador

# mensagem = ' Eu amo comida'
# print(mensagem.lower()) # eu amo comida
# print(mensagem.find('c')) #posicao 7
# print(mensagem.replace('Eu','vc')) # vc amo comida
# print(mensagem.strip()) #tira o espaço inicial

# operadores = 'banana' == 'Banana'
# teste = 10 > 9
# print(operadores) #false
# print(teste) #true

# velocidade = 4
# if velocidade > 12:
#     print('está acima')
# elif velocidade < 5:
#     print('dirigir mais rapido')
# else:
#     print('ok')
        
# renda_5mil = True
# nome_limpo = True

############################ Condicionantes
# if renda_5mil or nome_limpo:
#     resultado = print('financiamento aprovado')
# else:
#     resultado = print('financiamento negado')

# voto = 'voto permitido' if nome_limpo else 'voto não permitido'
# print(voto)

# soma = 5
# if 2 < soma < 10:
#     print('ok')

################## laços de repetição
# for numero in range(5): #01234
#     print(numero)

# for numero in range(1,5): #)1234
#     print(numero)

# for numero in range(1,5,3): #14
#     print(numero)

# for letra in 'Google':
#     print(letra)

# compra = False
# dados = 'compra de R$10'

# for i in range(2):
#     if compra:
#         print(dados)
#         break
#     else:
#         print('sem compra')
#         break

# palavra = 'TESTE'

# for space in palavra:
#     print(f' {space}', end='') # T E S T E
    
# for space in palavra:
#     print(f' ', end='') # 5 espaços
# print()
# for space in palavra:
#     print(space) #T
#                  #E
#                  #S
#                  #T
#                  #E
# for space in palavra:
#     print(space,end='')  #TESTE

linhas = 6
coluna = 6
simbolo = '*'

for l in range(linhas):
    for c in range(coluna):
        print(simbolo,end="")
    print()
''' 
Retangulo
******
******
******
******
******
******
'''

#valor = 100
valor = float(input('digite o valor do produto: '))
dia = 1
while valor > 20:
    dia +=1
    print(f' no dia {dia} o produto = {valor} ')
    
    valor -= 5