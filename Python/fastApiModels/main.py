from fastapi import FastAPI
from models.characterModel import Character
from data.characters import characters_dict




app = FastAPI()
apiName = "The Witcher Lib"



@app.get("/")
async def root():
    return {"message": "Welcome to API " + apiName}


@app.get("/characters")
async def getCharacter():
    if len(characters_dict) > 0:
        return characters_dict
    else:
        return "Não há personagens cadastrados"

# Rota para criar um personagem
@app.post("/characters/{new_character}")
def criar_personagem(character: Character):
    try:
        characters_dict.append(character)
        return {
            "mensagem": "Personagem criado com sucesso!",
            "dados": character
        }  
    except:
        return {"erro": "Erro ao criar personagem"}
    
@app.update("/characters/{character_id}")
def update_character(character_id: int):
    pass
