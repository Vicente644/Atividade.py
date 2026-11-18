import random

compradores = []

quantidade = int(input("Quantas rifas foram vendidas? "))

for i in range(quantidade):
  nome = input("Digite o nome do comprador: ")
  compradores.append(nome)

ganhador = random.choice(compradores)
print("O ganhador da rifa é:", ganhador)
