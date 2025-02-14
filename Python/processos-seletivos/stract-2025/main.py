from flask import Flask
import os
from dotenv import load_dotenv

from utils.utils import csv_to_html_table, str_to_html_content, download_csv


from api.reportPlataform import report_platform
from api.reportPlataformResume import report_platform_resume
from api.reportRoot import report_root
from api.reportGeneral import report_general
from api.reportGeneralResume import report_general_resume


from api.consumeAccounts import fetch_accounts
from api.consumeFields import fetch_fields
from api.consumeInsights import fetch_insights
from api.consumePlatforms import fetch_platforms

load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

app = Flask(__name__)

# Rota padrão da API
@app.route("/")
def get_info():
    nome, email, linkedin, github = report_root()
    html_response = str_to_html_content(nome, email, linkedin, github)
    return html_response


# Rotas de acesso aos dados
@app.route("/<platform>")
def get_platform(platform):
    data =report_platform(ACCESS_TOKEN, platform)
    html_response = csv_to_html_table(data)
    return html_response

@app.route("/<platform>/resumo")
def get_platform_general(platform):
    data = report_platform_resume(ACCESS_TOKEN, platform)
    html_response = csv_to_html_table(data)
    return html_response

@app.route("/geral")
def get_general():
    data = report_general(ACCESS_TOKEN)
    html_response = csv_to_html_table(data)
    return html_response

@app.route("/geral/resumo")
def get_general_resume():
    data = report_general_resume(ACCESS_TOKEN)
    html_response = csv_to_html_table(data)
    return html_response


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host="0.0.0.0", port=port)

