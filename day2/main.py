def Calc_IMC():
    if imc_valor < 18.5:
        print ("Atenção: Seu IMC indica que você está abaixo do peso ideal. É importante consultar um nutricionista.")   
    elif 18.5 <= imc_valor < 24.9:
        print ("Parabéns! Você está na faixa de peso normal. Continue mantendo hábitos saudáveis.")
    elif 25 <= imc_valor <29.9:
        print ("Sinal amarelo: Você está na faixa de sobrepeso. Pequenos ajustes na rotina podem ajudar.")
    else:
        print ("Cuidado: Seu IMC indica obesidade. Procure orientação médica para cuidar da sua saúde.")
print("Bem vindo a calculadora de IMC")
alt = float(input("Me diga sua altura: "))
pes = float(input("Me diga o seu peso: "))
imc_valor = pes / (alt **2)

def input_num():
    if imc_valor > 0:
        print(f"Seu IMC é {imc_valor:.2f}")
        return Calc_IMC()
    else:
        print ("só NÚMEROS positivos por favor!")

input_num()
