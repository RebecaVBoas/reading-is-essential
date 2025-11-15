from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReaderCreate(BaseModel):
    nome: str
    email: str
    telefone: Optional[str] = None
    endereco:Optional[str] = None

class ReaderUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    endereco:Optional[str] = None
    ativo: Optional[bool] = None
    
class ReaderResponse(BaseModel):
    id: int
    nome: str
    email: str
    telefone: Optional[str]
    endereco: Optional[str]
    data_cadastro: datetime
    ativo: bool

    class Config:
        from_attributes = True



