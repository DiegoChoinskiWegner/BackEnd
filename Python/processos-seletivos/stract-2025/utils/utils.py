import io
from flask import send_file

def csv_to_html_table(csv_data):
    rows = csv_data.strip().split("\n")
    table = "<table border='1'>"

    for row in rows:
        columns = row.split(",")
        table += "<tr>" + "".join(f"<td>{col.strip()}</td>" for col in columns) + "</tr>"

    table += "</table>"
    return table


def download_csv(output):
    csv_content = output
    
    csv_file = io.StringIO(csv_content)
    csv_file.seek(0)
    
    return send_file(io.BytesIO(csv_file.getvalue().encode('utf-8')), 
                        mimetype='text/csv',
                        as_attachment=True,
                        attachment_filename="relatorio.csv"
                    )


def str_to_html_content(nome, email, linkedin, github):
    message = f"""  <div style="font-family: Arial, sans-serif;text-align: center; 
                    margin: 50px auto; padding: 20px; 
                    max-width: 400px; border: 1px solid #ccc; 
                    border-radius: 10px;  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                        <p>Meu nome é <strong>{nome}</strong></p>
                        <p>Email: <strong>{email}</strong></p>
                        <p>Minhas redes são:</p>
                        <a href="{linkedin}" target="_blank" style="display: block; margin: 5px; color: #007BFF; text-decoration: none;">LinkedIn</a>
                        <a href="{github}" target="_blank" style="display: block; margin: 5px; color: #007BFF; text-decoration: none;">GitHub</a>
                        <p>Sinta-se à vontade para me contatar!</p>
                    </div>"""

    return message