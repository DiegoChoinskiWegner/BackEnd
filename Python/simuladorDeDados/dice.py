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

        if dice == 1:
            print("1")
        if dice == 2:
            print("2")
        if dice == 3:
            print("3")  
        if dice == 4:
            print("4")
        if dice == 5:
            print("5")
        if dice == 6:
            print("6")

        print ("\nDeseja jogar novamente?")
        resposta = int(input("1 - sim; 2 - não\n"))
        if resposta == 1:
            test = False
        else:
            test = True
            break




