# 1. Print e Variáveis
# Crie um programa que armazene o seu nome, sua idade e sua cidade em variáveis. Depois, exiba uma frase única no terminal usando essas variáveis.

# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
# cidade = input("Digite sua cidade: ")
# print(f'Olá. meu nome é {nome}, tenho meus {idade} anos de idade e moro em {cidade}.')
# 


# 2. Condicionais (if/else)
# Crie um programa que peça um número ao usuário (use input).

# Se o número for par, imprima: "O número é par".

# Se for ímpar, imprima: "O número é ímpar".

# Dica: Use o operador de módulo %.


# num= int(input("Digite um numero:"))
# if num % 2 == 0:
#     print("O número é par")
# else:
#     print("O número é ímpar")

# 3. Repetição (for)
# Crie um programa que imprima a tabuada do 5, do 1 ao 10, usando a estrutura for.

# Saída esperada:

# Plaintext
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

# tabuada = int(input("Digite um numero pra saber a tabuada: "))
# print(f"Tabuada de {tabuada}:")
# for i in range (1, 11):
#     resultado = tabuada * i"
#     print(f"resultado da tabuada de {tabuada} x {i} = {resultado}")




# 4. O "Combo" (for + if)
# Crie um loop que percorra os números de 1 a 20.

# Para cada número, o programa deve verificar:

# Se o número for maior que 10, imprima: "[Número] é maior que 10".

# Caso contrário, imprima: "[Número] é baixo".""


# for num in range(1, 21):
#     if num >= 10:
#         print(f"numero {num} é grande")
#     else:
#         print(f"numero {num} é pequeno")




# 1. Calculadora de Média (Variáveis + Print)
# Crie um programa que receba duas notas de um aluno (use input e float). Calcule a média e exiba a frase:
# Exemplo de saída: A média final é 7.5

# nota1 = float(input("Digite a sua primeira nota:"))
# nota2 = float(input("Digite a sua segunda nota:"))
# media = (nota1 + nota2 ) / 2
# print(f"Sua média é {media} ")




# 2. Controle de Acesso (if/else)
# Peça para o usuário digitar a idade.

# Se a idade for 18 ou mais, imprima: "Acesso liberado".

# Se for menor que 18, imprima: "Acesso negado".


# idade = int(input("Digite sua idade: "))
# if idade >= 18:
#     print("Acesso liberado!")
# else:
#     print("Acesso negado")





# 3. Contador Regressivo (for)
# Crie um loop que conte de 10 até 1.

# Dica: O range também pode contar para trás se você usar um terceiro número (o passo): range(10, 0, -1).

# Saída esperada:

# Plaintext
# 10
# 9
# ...
# 1

# for num in range(20,0,-1):
#     print(num)





# 4. Filtro de Números (for + if)
# Crie um loop que percorra os números de 1 a 15.

# O programa deve imprimir o número apenas se ele for maior que 5 E menor que 12.

# Dica: Use if num > 5 and num < 12:.

# for num in range(1,15):
#     if num > 5 and num < 12:
#         print(f"Numero {num} é maior q 5 e menor q 12")
    