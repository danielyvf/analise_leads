from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI()

DATA_FOLDER = r"C:\Users\dvent\OneDrive\Documentos\pipeline_sdr\resultados_finais"

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao servidor"}

@app.get("/leads/sdr")
def leads_por_sdr():
    df = pd.read_csv(os.path.join(DATA_FOLDER, "leads_por_sdr.csv"))
    return df.to_dict(orient="records")

@app.get("/leads/origem")
def leads_por_origem():
    df = pd.read_csv(os.path.join(DATA_FOLDER, "leads_por_origem.csv"))
    return df.to_dict(orient="records")

@app.get("/leads/cargo")
def leads_por_cargo():
    df = pd.read_csv(os.path.join(DATA_FOLDER, "leads_por_cargo.csv"))
    return df.to_dict(orient="records")

@app.get("/leads/mes")
def leads_por_mes():
    df = pd.read_csv(os.path.join(DATA_FOLDER, "leads_por_mes.csv"))
    return df.to_dict(orient="records")
