from sqlalchemy import Column,ForeignKey, Integer, Date, Enum
from src.config.database import Base
from sqlalchemy.orm import relationship  # ← Para relationship

class Loan(Base):
    __tablename__ = "emprestimo"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    livro_id = Column(Integer,ForeignKey("livros.id") )
    leitor_id = Column(Integer, ForeignKey("leitor.id"))
    data_emprestimo = Column(Date)
    data_devolucao_prevista = Column(Date)
    data_devolucao_real =Column(Date)
    status = Column(Enum('ativo', 'devolvido', 'atrasado'))

    livro = relationship("Book", back_populates="emprestimos")
    leitor = relationship("Reader", back_populates="emprestimos")