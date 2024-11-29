import json
from azure.storage.blob import BlobServiceClient
from functions.document_ai_reader import extract_text_from_file


# Configurações do Azure Blob Storage
AZURE_CONNECTION_STRING = "seu_connection_string_aqui"
BUCKET_NAME = "nome_do_bucket"

# Função para processar o arquivo e salvar o JSON no bucket
def process_and_save_json(blob.name, file_content):
    try:
        # Extrai o conteúdo do arquivo (exemplo para PDFs)
        extracted_text = extract_text_from_file(blob.name, file_content)

        # Gera o JSON bruto com os dados extraídos
        data = {"file_name": blob.name, "content": extracted_text}
        json_data = json.dumps(data, indent=4, ensure_ascii=False)

        # Conecta ao serviço de blob
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(BUCKET_NAME)

        # Define o caminho da nova pasta no bucket (ex: 'processed/')
        new_blob_name = f"processed/{blob.name}.json"

        # Envia o JSON para o bucket
        blob_client = container_client.get_blob_client(new_blob_name)
        blob_client.upload_blob(json_data, overwrite=True)

        print(f"JSON salvo com sucesso em: {new_blob_name}")
        return new_blob_name
    except Exception as e:
        print(f"Erro ao processar e salvar JSON: {e}")
        return None