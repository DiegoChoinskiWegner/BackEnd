from functions.document_reader import monitor_bucket
from functions.document_ai_reader import extract_text_from_file
from functions.save_document import process_and_save_json


# Configurações do Azure Blob Storage
AZURE_CONNECTION_STRING = "seu_connection_string_aqui"
BUCKET_NAME = "nome_do_bucket"


# Executa o monitoramento
if __name__ == "__main__":
    monitor_bucket()