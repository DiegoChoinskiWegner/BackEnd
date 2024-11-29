from PyPDF2 import PdfReader

def upload_pdf(caminho_pdf):
    """
    Lê o conteúdo de um arquivo PDF e retorna como uma string.
    
    :param caminho_pdf: Caminho do arquivo PDF.
    :return: Conteúdo do PDF como uma string.
    """
    try:
        # Carregar o arquivo PDF
        leitor = PdfReader(caminho_pdf)
        
        # Inicializar uma variável para armazenar o texto
        texto_extraido = ""
        
        # Iterar por todas as páginas do PDF e extrair o texto
        for pagina in leitor.pages:
            texto_extraido += pagina.extract_text()
        
        return texto_extraido
    except Exception as e:
        return f"Erro ao processar o PDF: {e}"