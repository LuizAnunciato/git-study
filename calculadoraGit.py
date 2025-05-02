# Exemplo de código Python para calcular a soma de dois números
n1 = int(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
n2 = int(input("Digite o segundo número: "))

if operacao == "+":
    resultado = (n1 + n2)
elif operacao == "-":
    resultado = (n1 - n2)
elif operacao == "*":
    resultado = (n1 * n2)
elif operacao == "/":
    resultado = (n1 / n2)
else:
    resultado = "Operação inválida"

print("O resultado é:", resultado)
