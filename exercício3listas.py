palavras = []
palavra_maior = ""
for n in range(5):
    palavra_escolhida = input("Digite uma palavra: ")
    palavras.append(palavra_escolhida)
    if n == 0:
        palavra_maior = palavra_escolhida
    elif len(palavra_escolhida) > len(palavra_maior):
        palavra_maior = palavra_escolhida
print(f"A maior palavra é: {palavra_maior} com {len(palavra_maior)} caractéres.")