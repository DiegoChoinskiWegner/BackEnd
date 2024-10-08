from tkinter import *
import tkinter as tk

# Declara as variáveis globais
count = 0


##teste de função
def aumentarContador():
    global count 
    count += 1
    label['text'] = str(count)


#Criação de tela
janela = tk.Tk()
janela.title("Dados")
janela.config(padx=200, pady=180) 

#Texto inicial
texto = tk.Label(janela, text="Teste de contador de cliques")
#texto.grid(ipadx=30, ipady=90)

#botão de jogar o dado
botao = tk.Button(janela, text="Jogar Dado", command=aumentarContador)

#botao.grid(column=0, row=1, padx=10, pady=10)

# Cria o rótulo
label = tk.Label(janela, text='0')

# Adiciona o botão e o rótulo à janela
botao.pack()
label.pack()

# Exibe a janela
janela.mainloop()



