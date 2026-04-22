#nome = input('escreva seu nome:  ')
#print('prazer em te conhecer {:=^20}'.format(nome))
n1=int(input('escreva o primeiro numero: '))
n2=int(input('escreva o segundo numero: '))
s=n1+n2
b=n1-n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
so=n1%n2
print('o resultado da soma é: {:-^20}'.format(s), end=' ')#end='' --> junta linhas
print('o resultado da subtração é: {:-^20}'.format(b))
print('o resultado do produto é: {:-^20}'.format(m))
print('o resultado da divisão é: {:-^20}'.format(d))
print('o resultado da divisão inteira é: {:-^20}'.format(di))
print('o resultado da potência é: {:-^20}'.format(e))
print('o resultado da sobra é: {:-^20}'.format(so))