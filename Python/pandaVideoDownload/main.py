import requests
from bs4 import BeautifulSoup
import re

# URL do vídeo que você deseja baixar (substitua pela URL real)
video_url = "https://www.youtube.com/watch?v=RIDQraaiQWc"

# Faz a requisição à página do vídeo
response = requests.get(video_url)
if response.status_code == 200:
    # Parseia o conteúdo da página usando o BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Encontra os elementos de script que podem conter informações sobre o vídeo
    script_elements = soup.find_all("script")

    # Procura o elemento de script que contém a URL do vídeo
    video_script = None
    for script in script_elements:
        if "VIDEO_CONFIG" in script.text:
            video_script = script.text
            break

    if video_script:
        # Extrai a URL do vídeo usando expressões regulares
        video_url_match = re.search(r'"url":"(.*?)"', video_script)
        if video_url_match:
            video_url = video_url_match.group(1)
            print("URL do vídeo:", video_url)

            # Agora você pode usar bibliotecas para baixar o vídeo, como 'requests' ou 'wget'
            # Exemplo com 'requests':
            video_data = requests.get(video_url).content
            with open("video.mp4", "wb") as f:
                f.write(video_data)
            print("Vídeo baixado com sucesso.")
        else:
            print("URL do vídeo não encontrada.")
    else:
        print("Script do vídeo não encontrado.")
else:
    print("Erro ao acessar a página do vídeo:", response.status_code)
