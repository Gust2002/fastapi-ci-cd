from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel 

from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine("sqlite:///mydata.db")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
Base.metadata.create_all(bind=db)

app = FastAPI()

@app.get("/")
def Hello_World():
    return {"message": "Hello Guys, How you all doing?"}

meus_livros = {}

class Livro(BaseModel):
  nome_livro: str
  autor_livro: str 
  apelido_livro: str 
  ano_livro: int 
    
@app.get("/buscar")
def get_livro():
    if not meus_livros:
        return {"message": "Nao existe nenhum livro"}
    else:
        return {"message": meus_livros}
    
@app.post("/adicionar")
def post_livros(id_livro: int, livro: Livro):
    if id_livro in meus_livros:
        raise HTTPException(status_code=400,detail="Esse livro ja existe no banco de dados")
    else:
        meus_livros[id_livro] = livro.dict()
        
        return {"message": "Esse livro foi criado com sucesso"}
    
@app.put("/atualiza/{id_livro}")
def put_livros(id_livro: int, livro: Livro):
    livro = meus_livros.get[id_livro]
    if not livro:
        raise HTTPException(status_code=404,detail="Esse livro nao existe no banco de dados")
    else:
     meus_livros[id_livro] = livro.dict()
            
    return {"message": "Seu livro foi criado com sucesso"}
    
@app.delete("/deletar/{id_livro}")
def deletar_livro(id_livro: int):
    if id_livro not in meus_livros:
        raise HTTPException(status_code=500,detail="Esse livro nao existe no banco de dados")
    else:
       del meus_livros[id_livro]
       return {"message": "Esse livro foi deletado com sucesso"}   