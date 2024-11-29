import random
from tkinter import *
import tkinter as tk


## Geração de numero aleatório do dado e validação de continuação
test = False
dice = 0

while (test == False):
    for x in range(1):
        # Dado de 6 posições, troque o segundo valor para aumentar o tamanho do dado.
        dice = random.randint(1,6)

        print(dice)

        print ("\nDeseja jogar novamente?")
        resposta = int(input("1 - sim; 2 - não\n"))
        if resposta == 1:
            test = False
        else:
            test = True
            break




