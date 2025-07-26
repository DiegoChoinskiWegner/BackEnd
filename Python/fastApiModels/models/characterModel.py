from pydantic import BaseModel
from typing import Optional

# Modelo de dados do personagem
class Character(BaseModel):
    name: str
    age: int
    characterClass: str
    local: Optional[str] = None
    book: Optional[str] = None

