"""O endpoint "/geral/resumo" deve trazer uma tabela similar, mas colapsando em uma única linha todas as linhas que forem da mesma plataforma. 
Caso as colunas seja numéricas, os dados devem ser somados. Caso sejam texto, a coluna pode ficar vazia na linha em questão 
(exceto nome da plataforma, que é o mesmo para todas as linhas agregadas da plataforma em questão)."""


import io
import csv

from api.consumePlatforms import fetch_platforms
from api.consumeAccounts import fetch_accounts
from api.consumeFields import fetch_fields
from api.consumeInsights import fetch_insights


def report_general_resume(access_token):
    # Criar buffer para armazenar CSV
    output = io.StringIO()
    writer = csv.writer(output)

    # Buscar plataformas disponíveis
    platform_list = fetch_platforms(access_token)
    platform_values = [item["value"] for item in platform_list]

    # Buscar campos disponíveis por plataforma
    total_fields = set()
    fields_per_platform = {}

    for platform in platform_values:
        fields_list = fetch_fields(access_token, platform)
        if not isinstance(fields_list, list):
            print(f"Erro: resposta inesperada de fetch_fields para {platform}: {fields_list}")
            continue  
        
        fields = [item['value'] for item in fields_list]
        fields_per_platform[platform] = fields
        total_fields.update(fields)

    # Garantir uma lista ordenada dos campos
    total_fields = list(total_fields)

    # Criar cabeçalho do CSV
    writer.writerow(["Platform", "Account Name"] + total_fields)

    # Dicionário para armazenar dados agregados por plataforma e conta
    aggregated_data = {}

    for platform in platform_values:
        accounts_list = fetch_accounts(access_token, platform)

        for account in accounts_list:
            acc_id = account['id']
            acc_name = account['name']
            acc_token = account['token']

            insights = fetch_insights(access_token, platform, acc_id, acc_token, *fields_per_platform[platform])

            # Criar chave única para agrupar os dados
            key = (platform, acc_name)

            if key not in aggregated_data:
                aggregated_data[key] = {field: 0 for field in total_fields}

            for insight in insights:
                for field in total_fields:
                    value = insight.get(field, 0)

                    if isinstance(value, (int, float)):  # Somar se for numérico
                        aggregated_data[key][field] += value
                    else:
                        aggregated_data[key][field] = " "  # Deixar vazio se não for numérico

                # Calcular "Cost per Click" se não estiver presente
                if "cost_per_click" in total_fields:
                    total_spend = aggregated_data[key].get("spend", 0)
                    clicks = aggregated_data[key].get("clicks", 0)

                    if clicks > 0:
                        aggregated_data[key]["cost_per_click"] = round(total_spend / clicks, 2)

    # Escrever dados agregados no CSV
    for (platform, acc_name), values in aggregated_data.items():
        row = [platform, acc_name] + [values.get(field, " ") for field in total_fields]
        writer.writerow(row)

    return output.getvalue()


