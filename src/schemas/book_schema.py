from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class BookCreater(BaseModel):
    titulo: str
    autor: str
    isbn: Optional[str] =None
    ano_publicacao: Optional[int] = None
    editora: Optional[str] = None
    disponivel_para_emprestimo: Optional[bool] = True

class BookUpdate: 
    titulo: Optional[str] = None
    autor: Optional[str] = None
    isbn: Optional[str] = None
    ano_publicacao: Optional[str] = None
    editora: Optional[str] = None
    disponivel_para_emprestimo: Optional[bool] = None

class BookResponse:
    id: int
    tittulo: str
    autor: str
    isbn: Optional[str]
    ano_publicacao: Optional[int]
    editora: Optional[str]
    disponivel_para_emprestimo: bool
    data_cadastro: datetime

    class Config:
        from_attributes = True  

      