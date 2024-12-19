import math
import random

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

# Algoritmo Simulated Annealing
def simulated_annealing(initial_guess, temperature=1000, cooling_rate=0.95, tolerance=1e-2, max_iterations=1000):
    current_guess = initial_guess
    current_value = abs(lucro_liquido(current_guess))

    best_guess = current_guess
    best_value = current_value

    for _ in range(max_iterations):
        # Diminuir a temperatura
        temperature *= cooling_rate
        if temperature <= 1e-3:
            break

        # Gerar um novo vizinho (aleatório próximo do atual)
        next_guess = current_guess + random.uniform(-50, 50)  # Vizinhança maior
        next_guess = max(next_guess, 0)  # Garantir que o número de clientes não seja negativo
        next_value = abs(lucro_liquido(next_guess))

        # Critério de aceitação
        delta = next_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            current_guess = next_guess
            current_value = next_value

            # Atualizar a melhor solução encontrada
            if current_value < best_value:
                best_guess = current_guess
                best_value = current_value

        # Critério de parada
        if best_value < tolerance:
            break

    return best_guess

# Chamada do algoritmo
initial_guess = 100  # Chute inicial para o número de clientes
resultado = simulated_annealing(initial_guess)

print(f"Número ideal de clientes para break-even: {resultado:.0f}")