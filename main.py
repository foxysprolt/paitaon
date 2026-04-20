from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que qualquer página acesse seu backend
    allow_methods=["*"],
    allow_headers=["*"],
)


imoveis = [
    {"id": 1, "titulo": "Apartamento Vila Mariana", "valor": 500000, "tipo":"venda"},
    {"id": 2, "titulo": "Apartamento em Santana", "valor": 2500, "tipo":"aluguel"},
    {"id": 3, "titulo": "Casa Vila Zack Nach", "valor": 1000000, "tipo":"venda"},
    {"id": 4, "titulo": "Apartamento Pompeia", "valor": 750000, "tipo":"venda"}
]

@app.get("/imoveis")
def listar_todos():
    return imoveis

@app.get("/imoveis/{imovel_id}")
def buscar_id(imovel_id: int):
    for item in imoveis:
        if item["id"]== imovel_id:
            return item
    return{"erro":"nada encontrado"}



    # estudar um pouco do query dps 
@app.get("/imoveis/busca/")
def filtrar_imoveis(tipo: str):

    resultado = [i for i in imoveis if i["tipo"] == tipo]
    
    if not resultado:
        return {"aviso": "Nenhum imóvel desse tipo encontrado"}
        
    return resultado