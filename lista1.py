#Ola de novo pestana, seria mt legal se voce realmente tivesse lendo isso e que não tenha problema ser de 1 a 100

import random

def cumprimento(texto):
    return f"Olá, {texto}"


def media_numeros_aleatorios():
    numeros = [random.randint(1, 100) for _ in range(7)]
    media = sum(numeros) / len(numeros)
    return media


mensagem = cumprimento("Erik Nonato Rolin")
print(mensagem)

media = media_numeros_aleatorios()
#print(media)
print(f"A média dos 7 números sorteados é: {media:.2f}")