from twilio.rest import Client

# Substitua pelas suas credenciais Twilio
account_sid = 'SEU_ACCOUNT_SID'
auth_token = 'SEU_AUTH_TOKEN'
from_whatsapp_number = 'whatsapp:+14155238886'  # número oficial de teste da Twilio
to_whatsapp_number = 'whatsapp:+55SEUNUMERO'    # Seu número com DDI 

client = Client(account_sid, auth_token)

for i in range(1, 4):
    audio_path = f'mic_{i}.wav'
    message = client.messages.create(
        from_=from_whatsapp_number,
        body=f'Áudio do microfone {i}',
        media_url=f'https://SEU_HOST/mic_{i}.wav',  # Arquivo precisa estar hospedado publicamente
        to=to_whatsapp_number
    )
    print(f'Mensagem enviada com SID: {message.sid}')
