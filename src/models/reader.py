from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Text
from src.config.database import Base 
from sqlalchemy.sql import text  # ← Para server_default
from sqlalchemy.orm import relationship  # ← Para relationship

class Reader(Base):
    __tablename__ = "leitor"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(100))
    email = Column(String(150), unique=True)
    telefone = Column(String(20))
    endereco = Column(Text)
    data_cadastro = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    ativo = Column(Boolean, default=True)

    

    emprestimos = relationship("Loan", back_populates="leitor") 