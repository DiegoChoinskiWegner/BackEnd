from functions.tradutor_texto import traduzir_texto
from functions.upload_documento import upload_pdf




# Testando a tradução
print('Digite "texto" para digitar o que quer traduzir, ou "documento" para traduzir um documento:')
try:
    input_usuario = input("\n Opção:")
    if input_usuario == "texto":
        texto_original = input()
    elif input_usuario == "documento":
        caminho_pdf = input()
        texto_original = upload_pdf(caminho_pdf)
except:
    print("Digite uma opção válida")

idioma_para = "pt-br"  # Traduzir para inglês
resultado = traduzir_texto(texto_original, idioma_para)

print(f"Texto traduzido: {resultado}")
