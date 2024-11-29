import requests
from dotenv import load_dotenv
import os

load_dotenv()


# Configurações do Azure Translator
SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
ENDPOINT = os.getenv("ENDPOINT")
LOCATION = os.getenv("LOCATION")


def traduzir_texto(texto, idioma_destino, idioma_origem="en"):
    """
    Função para traduzir texto usando a API do Translator.
    :param texto: Texto para traduzir.
    :param idioma_destino: Código do idioma alvo (ex: 'en', 'es', 'pt').
    :param idioma_origem: Código do idioma de origem (opcional).
    :return: Texto traduzido.
    """
    url = f"{ENDPOINT}/translate"
    headers = {
        "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
        "Ocp-Apim-Subscription-Region": LOCATION,
        "Content-Type": "application/json"
    }
    params = {
        "api-version": "3.0",
        "to": idioma_destino,
    }
    if idioma_origem:
        params["from"] = idioma_origem
    
    body = [{"text": texto}]
    
    response = requests.post(url, headers=headers, params=params, json=body)
    response.raise_for_status()  # Levanta exceções se a requisição falhar
    traduzido = response.json()
    
    # Retorna apenas o texto traduzido
    return traduzido[0]["translations"][0]["text"]