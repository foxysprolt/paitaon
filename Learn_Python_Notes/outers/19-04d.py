def somacondaluguel(cond, alug):
    resultado = cond + alug
    return float(resultado)

# 1. Coletando os dados
nome = input('Coloque seu nome: ')
v_cond = float(input('Valor do Condomínio: '))
v_alug = float(input('Valor do Aluguel: '))

# 2. Agrupando em um Dicionário (Mindset de API)
usuario = {
    "nome": nome,
    "condominio": v_cond,
    "aluguel": v_alug
}

# 3. Processando
total_pagar = somacondaluguel(usuario["condominio"], usuario["aluguel"])

print(f"\nOlá {usuario['nome']}, o total é R$ {total_pagar:.2f}")

if total_pagar < 500:
    print("Status: Você está pagando muito pouco.")
else:
    print("Status: Você está pagando caro.")