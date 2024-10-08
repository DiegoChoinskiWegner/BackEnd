import json

data = json.load(open("data.json"))




print("Seja Bem Vindo ao dicionário de Phrasal Verbs!\n")
print("Escreva uma palavra ou frase para relaciona-la ao inglês")

interruptor = False
while interruptor == False:    
    try:
        resposta = str(input("-"))
    except:
        print("Digite uma palavra ou frase:")
    finally:
        if resposta in data:
            print(str(data[resposta]) + "\n")
        else:
            print("Palavra não encontrada\n")
        interruptorValidate = input("Deseja procurar outra palavra?")
        if interruptorValidate == "sim":
            interruptor = False
        else:
            interruptor = True
            print("Obrigado por usar nosso programa!")  
            break

     
    