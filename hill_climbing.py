# Dados fornecidos
custos_mensais = 38034.48
imposto_percentual = 16.50 / 100
custo_unitario = 51.62
ticket_medio = 400

# Função para calcular o lucro líquido
def lucro_liquido(clientes):
    receita = clientes * (ticket_medio * (1 - imposto_percentual))
    custos_variaveis = clientes * custo_unitario
    return receita - custos_variaveis - custos_mensais

# Algoritmo Hill Climbing
def hill_climbing(initial_guess, step_size=1, max_iterations=1000, tolerance=1e-2):
    current_guess = initial_guess
    current_value = abs(lucro_liquido(current_guess))

    for _ in range(max_iterations):
        # Testar soluções vizinhas
        next_guess = current_guess + step_size
        next_value = abs(lucro_liquido(next_guess))

        if next_value < current_value:  # Melhorou?
            current_guess = next_guess
            current_value = next_value
        else:  # Tentar o outro lado
            next_guess = current_guess - step_size
            next_value = abs(lucro_liquido(next_guess))
            if next_value < current_value:
                current_guess = next_guess
                current_value = next_value
            else:  # Nenhuma melhoria encontrada, parar
                break

        # Parar se a melhoria for menor que a tolerância
        if current_value < tolerance:
            break

    return current_guess

# Chamada do algoritmo
initial_guess = 100  # Chute inicial para o número de clientes
resultado = hill_climbing(initial_guess)

print(f"Número ideal de clientes para break-even: {resultado:.0f}")
