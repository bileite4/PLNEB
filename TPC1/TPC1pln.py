#AULA 1 PLN
from collections import Counter

#EXERCÍCIO 1

nome=input('Introduza o seu nome:')
print('Nome em maiúsculas:', nome.upper())

#EXERCÍCIO 2

lista=input('Introduza a lista de números separada por espaço e prima enter no final:')
pares=[]
y = lista.split(" ")
for i in y:
    if int(i)%2 == 0:
        pares.append(i)
print('Os números pares introduzidos na lista foram:', pares)

#EXERCÍCIO 3

nome=input('Introduza o nome do ficheiro:')
ficheiro=open(nome, 'r')
linhas=ficheiro.readlines()
#linhas=list(open(nome))
print('A lista invertida é:', linhas[::-1])

#EXERCÍCIO 4

nome=input('Introduza o nome do ficheiro:')
ficheiro=open(nome, 'r')
palavras = ficheiro.read().split()
contagem = Counter(palavras)
print('As 10 palavras mais frequentes, e o número de ocorrências são:')
for palavra, cont in contagem.most_common(10):
    print(f"{palavra}: {cont}")

#EXERCÍCIO 5

texto=input('Introduza o texto:')
for pontuacao in string.ponctuation:
    texto.replace(pontuacao,f"{pontuacao} ")
texto.lower()

#EXERCÍCIO 6

s=input('Introduza a string:')
print('Inverso:', s[::-1])

#EXERCÍCIO 7

s=input('Introduza a string:')
a=0
b=0
for i in s:
    if i =='a':
        a+=1
    elif i=='A':
        b+=1
print('Número de as:', a)
print('Número de As:', b)

#EXERCÍCIO 8

s=input('Introduza a string:')
min=s.lower()
vogais=0
for i in min:
    if i =='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vogais+=1
print('Número de vogais presentes:', vogais)

#EXERCÍCIO 9

nome=input('Introduza uma string:')
print('String em minúsculas:', nome.lower())

#EXERCÍCIO 10

nome=input('Introduza uma string:')
print('String em maiúsculas:', nome.upper())



