import sounddevice as sd
import soundfile as sf
import threading

# Duração da gravação em segundos
duration = 5  
sample_rate = 44100

# Dispositivos (IDs ou nomes dos microfones instalados no sistema)
microfones = [1, 2, 3]  # Altere de acordo com sua máquina

def gravar_audio(device_id, filename):
    print(f"Gravando do microfone {device_id} em {filename}")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16', device=device_id)
    sd.wait()
    sf.write(filename, audio, sample_rate)
    print(f"Gravação finalizada: {filename}")

# Cria e inicia as threads
threads = []
for i, mic_id in enumerate(microfones):
    t = threading.Thread(target=gravar_audio, args=(mic_id, f'mic_{i+1}.wav'))
    threads.append(t)
    t.start()

# Aguarda todas as gravações terminarem
for t in threads:
    t.join()
