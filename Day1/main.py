print("bem vindo a calculadora!") 

def calcular():
    if opcao == 1:
        celsius_valor = float(input("Digite os Graus Celsius para transforma-los em Fahrenheit: "))
        resultado =  (celsius_valor * 9/5) + 32
        return resultado
    
    elif opcao == 2:
        fahrenheit_valor = float(input("Digite os Graus Fahrenheit para transforma-los em Celsius: "))
        resultado = (fahrenheit_valor - 32) * 5/9
        return resultado
    
    elif opcao == 3:
        dolar_valor = float(input("Digite o valor em dolar para transformar em real: "))
        resultado = dolar_valor / 5
        return resultado
    
    elif opcao == 4:
        real_valor = float(input("Digite o valor em real para transformar em dolar: "))
        resultado = real_valor * 5
        return resultado
    
    else:
        print("Opção não existe!")

     
opcao = int(input("""Selecione uma opção:\n(1) transformar Celsius em Fahrenheit\n(2) transformar Fahrenhei em Celsius\n(3) Transformar Dolar em Real\n(4) Transformar Real em Dolar\n """))

print(calcular())
