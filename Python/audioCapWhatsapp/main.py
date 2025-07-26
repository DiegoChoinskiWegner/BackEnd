import tkinter as tk
from tkinter import messagebox
import threading

class GravadorApp:
    def __init__(self, master):
        self.master = master
        master.title("Gravador de Áudio - Evento")
        master.minsize(400, 400)

        

        self.gravando = False
        self.threads = []
        self.duracao = 60  # segundos (mude para o necessário)


        # Labels e Entradas
        tk.Label(master, text="Microfone 1:").grid(pady=30, row=0, column=0)
        self.mic1_entry = tk.Entry(master)
        self.mic1_entry.grid(pady=30, row=0, column=1)

        tk.Label(master, text="Microfone 2:").grid(pady=30, row=0, column=3)
        self.mic2_entry = tk.Entry(master)
        self.mic2_entry.grid(pady=30, row=0, column=4)

        tk.Label(master, text="Microfone 3:").grid(pady=30, padx=10, row=0, column=5)
        self.mic3_entry = tk.Entry(master)
        self.mic3_entry.grid(pady=30, padx=10, row=0, column=6)

        tk.Label(master, text="Nome do Grupo:").grid(pady=15, row=3, column=3)
        self.grupo_entry = tk.Entry(master)
        self.grupo_entry.grid(pady=15, row=3, column=4)

        # Botões
        self.iniciar_btn = tk.Button(master, text="Iniciar Gravação", command=self.iniciar_gravacao)
        self.iniciar_btn.grid(row=5, column=3)

        self.pausar_btn = tk.Button(master, text="Parar Gravação", command=self.parar_gravacao)
        self.pausar_btn.grid(row=5, column=4)

    def gravar_audio(self, device, filename):
        audio = sd.rec(int(self.duracao * 44100), samplerate=44100, channels=1, dtype='int16', device=int(device))
        sd.wait()
        sf.write(filename, audio, 44100)
        print(f"Gravação finalizada: {filename}")

    def iniciar_gravacao(self):
        if self.gravando:
            messagebox.showinfo("Aviso", "Já está gravando.")
            return

        try:
            mic1 = int(self.mic1_entry.get())
            mic2 = int(self.mic2_entry.get())
            mic3 = int(self.mic3_entry.get())
            grupo = self.grupo_entry.get()

            if not grupo:
                messagebox.showerror("Erro", "Digite o nome do grupo.")
                return

            self.gravando = True
            self.threads = []

            for i, mic in enumerate([mic1, mic2, mic3]):
                filename = f"{grupo}_mic{i+1}.wav"
                t = threading.Thread(target=self.gravar_audio, args=(mic, filename))
                self.threads.append(t)
                t.start()

            messagebox.showinfo("Gravando", "Gravação iniciada.")

        except ValueError:
            messagebox.showerror("Erro", "Certifique-se de digitar apenas IDs numéricos dos microfones.")

    def parar_gravacao(self):
        if not self.gravando:
            messagebox.showinfo("Aviso", "Nenhuma gravação em andamento.")
            return

        self.gravando = False
        messagebox.showinfo("Finalizado", "A gravação foi finalizada.")

# Inicializa a janela
root = tk.Tk()
app = GravadorApp(root)
root.mainloop()
