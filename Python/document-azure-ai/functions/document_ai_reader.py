import json
from azure.storage.blob import BlobServiceClient
from PyPDF2 import PdfReader  # Para leitura de PDFs


# Função para extrair texto do arquivo (atualmente suporta PDFs)
def extract_text_from_file(blob_name, file_content):
    try:
        if blob_name.lower().endswith(".pdf"):
            # Extrai texto de um arquivo PDF
            reader = PdfReader(file_content)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text.strip()

        elif blob_name.lower().endswith(".txt"):
            # Arquivo de texto simples
            return file_content.decode("utf-8").strip()

        else:
            raise ValueError("Formato de arquivo não suportado!")

    except Exception as e:
        print(f"Erro ao extrair texto do arquivo {blob_name}: {e}")
        return ""
