############# LISTAS ################
# cidade = ['Rio de janeiro','brasilia','São paulo']
# x = cidade.pop(1)

# print(cidade)
# print(x)

# cidade.append('Brasilia')
# cidade.sort()

# print(cidade)

# numero = [ 2,3,4,5]
# final = numero * 2 # repete 2 vezes

# print(final) #[2, 3, 4, 5, 2, 3, 4, 5]

# letras = ['a', 'b', 'c']
# final2 = numero + letras
# print(final2) #[2, 3, 4, 5, 'a', 'b', 'c']

# itens = [['item1','item2'],['item3','item4']]
# print(itens[1][0]) #item3

# letras = ['a', 'b', 'c']
# item1,item2,item3 = letras

# print(item1) #a
# print(item2) #b
# numero = [ 2,3,4,5]
# first, *outros = numero
# print(outros) #3,4,5

# if 'a' in letras:
#     print('sim') 
# else:
#     print('não')

# cores = ['amarelo','verde','azul','vermelho']
# valor = [10,20,30,40]

# # var = list('Andre')
# # print(var) #['A', 'n', 'd', 'r', 'e']

# duas_listas = zip(cores,valor)

# print(list(duas_listas))
# #[('amarelo', 10), ('verde', 20), ('azul', 30), ('vermelho', 40)]

# listas = zip(valor,cores)
# x = list(listas)

# print(x[0][1]) #amarelo

############ Tuple ##############
# cores_lista = ['amarelo','verde','azul','vermelho']
# #pode ser alterada, mas gasta mais espaço na memoria
# cores_tuple = ('amarelo','verde','azul','vermelho')
# #não pode ser alterada, mas gasta menos

# x = cores_tuple.__sizeof__

# print(x)


# ############# Array ############
# from array import array
# letras = ['a','b','c','d']
# numero_i = [10,20,30,40]
# numero_f = [1.2,2.2,3.2]

# letras = array('u',['a','b','c','d'])
# numero_i = array('i',[10,20,30,40])
# numero_f = array('f',[1.2,2.2,3.2])

# print(letras) #array('u', 'abcd')
# print(numero_i)
# print(numero_f)

# ############# set(Listas) #########
# list1 = [10,20,30,40,50]
# list2 = [10,20,60,70]

# num1 = set(list1)
# num2 = set(list2)

# print(num1) #{40, 10, 50, 20, 30} perdeu indexação
# print(num1 | num2) # {70, 40, 10, 50, 20, 60, 30} 
# #sem repetição de valores, união

# print(num1 - num2) #{40, 50, 30}
# # elimina os valores que estão iguais do primeiro
# # para o segundo, subtração 

# print(num1 ^ num2) #{70, 40, 50, 60, 30}
# #soma os valores e elimina os valores iguais

# print(num1 & num2) #{10, 20}
# # só os numeros em comum da lista

# print(len(num1)) #5
# #tamanho

# ## obs: n existe num1[i] ,porque não tem indexação

list1 = [1,2,3,5,6] # type = lista
set1 = {1,2,3,5,6} # type = set

set1.add(4)
print(set1) #{1, 2, 3, 4, 5, 6}

set2 = {1,2,3,3,3,4,5,5,6}
print(set2) # {1, 2, 3, 4, 5, 6}
# Evita itens duplicados
set2.update([6,7,8,9,9])
print(set2) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
#set1.remove(12) = gera um erro pois n tem esse
#set1.discard(12) = não gera erro mesmo n tendo
#os dois eliminam elementos