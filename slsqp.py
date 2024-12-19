from scipy.optimize import minimize

# Dados fornecidos
custos_mensais = 38034.48
imposto_percentual = 16.50 / 100
custo_unitario = 51.62
ticket_medio = 400

# Função de custo que representa o prejuízo (devemos minimizá-la)
def prejuizo(clientes):
    receita = clientes * (ticket_medio * (1 - imposto_percentual))
    custos_variaveis = clientes * custo_unitario
    lucro_liquido = receita - custos_variaveis - custos_mensais
    return abs(lucro_liquido)  # O objetivo é zerar o prejuízo

# Restrição: o lucro líquido deve ser zero (break-even)
def restricao(clientes):
    receita = clientes * (ticket_medio * (1 - imposto_percentual))
    custos_variaveis = clientes * custo_unitario
    lucro_liquido = receita - custos_variaveis - custos_mensais
    return lucro_liquido

# Ponto inicial (chute inicial para o número de clientes)
chute_inicial = [100]

# Configurando as restrições e limites
restricoes = {"type": "eq", "fun": restricao}
limites = [(0, None)]  # Número de clientes não pode ser negativo

# Otimização utilizando SLSQP
resultado = minimize(prejuizo, chute_inicial, method="SLSQP", bounds=limites, constraints=restricoes)

# Resultado final
clientes_otimizados = round(resultado.x[0])
print(f"Número ideal de clientes para break-even: {clientes_otimizados}")
