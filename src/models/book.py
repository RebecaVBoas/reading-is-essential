from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from src.config.database import Base

class Book(Base):
    __tablenamme__= "livros"

    id = Collum(Integer, primary_key= True,index=True, autoincrement = True )
    titulo = Column(String(200), unique=True)
    autor = Column(String(100))
    isbn = Column(String(20))
    ano_publicacao=Column(Integer)
    editora = Column(String(100))
    disponivel_para_emprestimo = Column(Boolean, default=True)
    data_cadastro = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    emprestimo = relationship("Loan", back_populates="livro")