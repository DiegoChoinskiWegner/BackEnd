"""Uma exceção é o campo "cost_per_click", 
que não está disponível para esta API no Google Analytics, porém pode ser calculado dividindo-se o valor de "spend" pelo valor de "clicks"."""


import io
import csv

from api.consumePlatforms import fetch_platforms
from api.consumeAccounts import fetch_accounts
from api.consumeFields import fetch_fields
from api.consumeInsights import fetch_insights



def report_general(access_token):
    # Cria variavel para escrever a saida no formato csv
    output = io.StringIO()
    writer = csv.writer(output)

    # Recebe os dados da Plataforma escolhida
    platform_list = fetch_platforms(access_token)
    platform_values = []
    for item in platform_list:
        platform_values.append(item["value"])

    
    # Recebe a lista de campos (fields) dos anuncios dessa plataforma 
    total_fields=set()
    fields_per_platform = {}
    for platform in platform_values:
        fields_list = fetch_fields(access_token, platform)
        fields = []
        if not isinstance(fields_list, list):  
            print(f"Erro: resposta inesperada de fetch_fields para {platform}: {fields_list}")
            continue  
        for item in fields_list:
            fields.append(item['value'])
            total_fields.update(fields)
        fields_per_platform[platform]=fields

    # Cria cabeçalho da saída
    total_fields = list(total_fields)
    writer.writerow(["Platform"] + total_fields + ["Account Name"])

    seen_rows = set()

    for platform in platform_values:
        accounts_list = fetch_accounts(access_token, platform)
        accounts = []

        for account in accounts_list:
            accounts.append({"id": account['id'], "name": account['name'], "token": account['token']})

            for acc in accounts:
                insights = fetch_insights(access_token, platform, acc['id'], acc['token'], *fields_per_platform[platform])

                for insight in insights:
                    insight_values = [insight.get(field, "") for field in total_fields]
                    cpc_index = total_fields.index("cost_per_click")

                    if not insight.get("cost_per_click"):
                        total_spend = float(insight.get("spend") or 0.0)  # Converte None ou string para float
                        clicks = float(insight.get("clicks") or 0.0)

                        if clicks > 0:
                            cost_per_click = round(total_spend / clicks, 2)
                            insight_values[cpc_index] = cost_per_click
                    




                    # Criar uma tupla com os dados para evitar linhas duplicadas
                    row_tuple = tuple(([platform] + insight_values + [acc["name"]]))

                    if row_tuple not in seen_rows:  # Verifica se a linha já foi adicionada
                        seen_rows.add(row_tuple)
                        writer.writerow(row_tuple)

    return output.getvalue()
