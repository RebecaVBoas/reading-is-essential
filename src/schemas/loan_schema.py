from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime


class LoanCreate(BaseModel):
    livro_id: int
    leitor_id: int
    data_devolucao_prevista: date

class LoanUpdate(BaseModel):
    data_devolucao_prevista: Optional[date] = None
    data_devolucao_real: Optional[date] = None
    status: Optional[str] = None

class LoanResponse(BaseModel):
    id: int
    livro_id: int
    leitor_id: int
    data_emprestimo: date
    data_devolucao_prevista: date
    data_devolucao_real: Optional[date] = None     
    status: str

    class Config:
        from_attributes = True  