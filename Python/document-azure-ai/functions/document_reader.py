from azure.storage.blob import BlobServiceClient
import time
from functions.document_ai_reader import extract_text_from_file
from functions.save_document import process_and_save_json


# Configurações do Azure Blob Storage
AZURE_CONNECTION_STRING = "seu_connection_string_aqui"
BUCKET_NAME = "nome_do_bucket"

# Função para monitorar o bucket
def monitor_bucket():
    # Conecta ao serviço de blob
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(BUCKET_NAME)

    # Lista de arquivos já processados
    processed_files = set()

    print(f"Iniciando monitoramento do bucket '{BUCKET_NAME}'...")
    while True:
        try:
            # Lista blobs no container
            blobs_list = container_client.list_blobs()
            for blob in blobs_list:
                if blob.name not in processed_files:
                    print(f"Novo arquivo detectado: {blob.name}")

                    # Faz o download do arquivo
                    blob_client = container_client.get_blob_client(blob.name)
                    file_content = blob_client.download_blob().readall()

                    # Processa o arquivo com a função document_ai_reader
                    extract_text_from_file(blob.name, file_content)

                    # Marca como processado
                    processed_files.add(blob.name)

                    process_and_save_json(blob.name, file_content)

            # Espera antes de verificar novamente
            time.sleep(10)

        except Exception as e:
            print(f"Erro ao monitorar o bucket: {e}")

