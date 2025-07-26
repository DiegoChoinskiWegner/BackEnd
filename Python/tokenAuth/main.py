from flask import Flask, request, jsonify
import pyotp
import qrcode
import io
import base64

app = Flask(__name__)

# Simulando um "banco de dados" em memória
users = {}

@app.route('/', methods=['GET'])
def startApi():
    return "API rodando"


@app.route('/register-mfa', methods=['POST'])
def register_mfa():
    username = request.json.get('username')

    # Gerar chave secreta TOTP
    secret = pyotp.random_base32()

    # Criar URL compatível com o Google Authenticator
    totp = pyotp.TOTP(secret)
    otpauth_url = totp.provisioning_uri(name=username, issuer_name="MinhaApp")

    # Gerar QR Code como imagem base64
    img = qrcode.make(otpauth_url)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_code_b64 = base64.b64encode(buffer.getvalue()).decode()

    # Salvar usuário e chave secreta
    users[username] = {
        'secret': secret
    }

    return jsonify({
        "message": "Escaneie este QR Code com o Google Authenticator",
        "qr_code_base64": f"data:image/png;base64,{qr_code_b64}",
        "secret": secret  # só exiba isso para testes
    })

@app.route('/verify-mfa', methods=['POST'])
def verify_mfa():
    data = request.json
    username = data.get('username')
    token = data.get('token')

    user = users.get(username)
    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404

    totp = pyotp.TOTP(user['secret'])

    if totp.verify(token, valid_window=1):
        return jsonify({"message": "MFA verificado com sucesso!"})
    else:
        return jsonify({"message": "Código inválido"}), 401

if __name__ == '__main__':
    app.run(debug=True)
    