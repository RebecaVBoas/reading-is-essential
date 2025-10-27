from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+mysqlconnector://beca:123@localhost/lep"


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()


#Função que o FastAPI usara para obter sessões do banco.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()