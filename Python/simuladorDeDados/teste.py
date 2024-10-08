# Importa o módulo Tkinter
import tkinter as tk

# Declara as variáveis globais
contador = 0

# Define a função que é chamada quando o botão é clicado
def clicar():
    global contador
    contador += 1
    label['text'] = str(contador)

# Cria a janela principal
janela = tk.Tk()

# Cria o botão
botao = tk.Button(janela, text='Clicar', command=clicar)

# Cria o rótulo
label = tk.Label(janela, text='0')

# Adiciona o botão e o rótulo à janela
botao.pack()
label.pack()

# Exibe a janela
janela.mainloop()
