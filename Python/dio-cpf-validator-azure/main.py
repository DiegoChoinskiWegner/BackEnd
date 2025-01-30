import logging
import requests
import azure.functions as func

def validar_cpf(cpf):
    # Lógica de validação do CPF (exemplo simplificado)
    # Você pode usar bibliotecas como 'validate_docbr' para uma validação mais robusta
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove caracteres não numéricos
    if len(cpf) != 11:
        return False
    return True

def verificar_restricoes_cpf(cpf):
    # Lógica para consultar a API da Receita Federal
    # Ajustar endpoint real da fazenda para acessar cpf
    url = f"http://cpf.receita.fazenda.gov.br/situacao/{cpf}"  # Exemplo de URL
    headers = {
        "Authorization": "Bearer SUA_CHAVE_API" 
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Avaliar posteriormente como vem a resposta Json do ministério da Fazenda
            data = response.json()
            return data.get(f"O cpf {cpf} possui as seguintes restrições: {data}")  
        else:
            return None  # Erro na consulta
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na consulta da API: {e}")
        return None
    finally:
        response.close()


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger da função em python está processando a requisição')

    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')

    if cpf:
        if validar_cpf(cpf):
            restricoes = verificar_restricoes_cpf(cpf)
            if restricoes is not None:
                return func.HttpResponse(
                     f"CPF: {cpf}, Restrições: {restricoes}",
                     mimetype="application/json"
                )
            else:
                return func.HttpResponse(
                     "Erro ao consultar API da Receita Federal",
                     status_code=500
                )
        else:
            return func.HttpResponse(
                 "CPF inválido",
                 status_code=400
            )
    else:
        return func.HttpResponse(
             "Informe o CPF no parâmetro 'cpf'",
             status_code=400
        )