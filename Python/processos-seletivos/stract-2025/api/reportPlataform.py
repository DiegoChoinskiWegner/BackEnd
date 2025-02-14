import io
import csv

from api.consumePlatforms import fetch_platforms
from api.consumeAccounts import fetch_accounts
from api.consumeFields import fetch_fields
from api.consumeInsights import fetch_insights

def report_platform( access_token, platform):
    # Cria variavel para escrever a saida no formato csv
    output = io.StringIO()
    writer = csv.writer(output)

    # Recebe os dados da Plataforma escolhida
    platform_list = fetch_platforms(access_token)
    platform = platform.lower().replace(" ", "")
    for item in platform_list:
        item['text'] = item['text'].lower().replace(" ", "")
        if item['text'] == platform:
            platform = item['value']
        else:
            pass

    
    # Recebe a lista de campos (fields) dos anuncios dessa plataforma 
    fields_list = fetch_fields(access_token, platform)
    fields = []
    for item in fields_list:
        fields.append(item['value'])

    # Cria cabeçalho da saída
    writer.writerow(["Platform"] + fields + ["Account Name"])

    accounts_list = fetch_accounts(access_token, platform)
    accounts = []

    for item in accounts_list:
        accounts.append({"id": item['id'], "name": item['name'], "token": item['token']})
    
    for item in accounts:
        insights = fetch_insights(access_token, platform, item['id'], item['token'], *fields)
        for insight in insights:
            insight_values = [insight.get(field, "") for field in fields]
            writer.writerow([platform] + insight_values + [item["name"]])

    return output.getvalue()

