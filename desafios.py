CONSTANTE_BONUS = 1000

# 1. Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

if nome_usuario.isdigit():
    print("Você digitou seu nome errado.")
elif len(nome_usuario) == 0:
    print("Você não digitou nenhum nome.")
elif nome_usuario.isspace():
    print("Você digitou apenas espaço.")

# 2. Solicita ao usuário que digite o valor do seu salário
# e converte a entrada para um número de ponto flutuante.
salario_usuario = float(input("Digite o seu salário: "))

# 3. Solicita ao usuário que digite o valor do bônus recebido
# e converte a entrada para um número de ponto flutuante.
bonus_usuario = float(input("Digite o seu bônus: "))

# 4. Calcule o valor do bônus final
valor_bonus = CONSTANTE_BONUS + salario_usuario + bonus_usuario

# 5. Imprime a mensagem personalizada incluindo o 
# nome do usuário e o valor do bônus
print(f"O usuário {nome_usuario.capitalize()} receberá um bônus de R$ {valor_bonus:.2f}")
