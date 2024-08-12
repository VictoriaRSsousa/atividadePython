# Escreva uma função em Python que recebe uma lista e retorna uma nova lista com os elementos únicos da lista inicial.
# Lista Exemplo : [1,2,3,3,3,3,4,5]
# Saída : [1, 2, 3, 4, 5]

lista = [1,2,3,3,3,3,4,5,7,3]
listaDeRetorno = []

for numero in lista:
    if numero not in listaDeRetorno:
        listaDeRetorno.append(numero)
    
print(listaDeRetorno)

#         ------------------------------------------------------------------------------   
# Escreva um programa que retorna se dois dicionários possuem o mesmo item.
# Exemplo: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Resultado: key1: 1 está presente em x e y

dicionario1 = {'key1': 1, 'key2': 3, 'key3': 2}
dicionario2 = {'key1': 1, 'key2': 2}

for item1 in dicionario1:
    for item2 in dicionario2:
        if dicionario1[item1] == dicionario2[item2] and item1 == item2:
            print(dicionario1[item1],dicionario2[item2])
            print(item1 + " : " + str(dicionario1[item1]) + " está presente em dicionario1 e dicionario2" )
            
#         ------------------------------------------------------------------------------            
# Escreva um programa em Python que seleciona os itens ímpares em uma lista.
# Lista Exemplo : [1,5,7,3,10,14,21,22]
# Resultado: [1,5,7,3,21] 

lista = [1,5,7,3,10,14,21,22]    
impares = []

for numero in lista :
    if numero%2!=0:
      impares.append(numero)     
      
print(impares)        
#         ------------------------------------------------------------------------------                        
#  Escreva uma função em Python que recebe uma string e calcula o número de letras maiúsculas e minúsculas na mesma.
# String Exemplo: 'Ordem e Progresso'
# Resultado Esperado : 
# No. de letras maiúsculas : 2
# No. de letras minúsculas : 13

string = 'Ordem e Progresso'
letrasMaiusculas = 0
letrasMinusculas = 0

for letra in string:
    if letra.isupper():
        letrasMaiusculas +=1
    if letra.islower():
        letrasMinusculas +=1
#         ------------------------------------------------------------------------------               
# print("No. de letras maiúsculas : " + str(letrasMaiusculas))
# print("No. de letras minúsculas : " + str(letrasMinusculas))     

# Escreva uma função em Python que retorna uma string reversa.
# Exemplo Entrada : "1234abcd"
# Exemplo Saída : "dcba4321"  

entrada =  "1234abcd"
saida = ""
 
for letra in entrada :
    saida = letra + saida
    
print(saida)    