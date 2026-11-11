#exercício 1
numeros = []
impares = []
pares = []

for i in range(10):
    num_escolhido = int(input("digite um número:"))
    numeros.append(num_escolhido)

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Quantidade de pares {len{pares}}")
print(f"quantidade de ímpares {len{impares}}")

#exercício 2
