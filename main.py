from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Permitir CORS para que el frontend pueda hacer peticiones
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas a los archivos CSV
archivo_cdmx = 'conagua/CDMX.csv'
archivo_edomex = 'conagua/ESTADO DE MEXICO.csv'

def calcular_riesgo(df):
    df['PRECIP(MM)'] = pd.to_numeric(df['PRECIP(MM)'], errors='coerce').fillna(0)
    df['EVAP(MM)'] = pd.to_numeric(df['EVAP(MM)'], errors='coerce').fillna(0)
    df['TMAX(C)'] = pd.to_numeric(df['TMAX(C)'], errors='coerce').fillna(0)
    df['TMIN(C)'] = pd.to_numeric(df['TMIN(C)'], errors='coerce').fillna(0)

    df['balance_hidrico'] = df['PRECIP(MM)'] - df['EVAP(MM)']
    df['rango_termico'] = df['TMAX(C)'] - df['TMIN(C)']
    df['riesgo_inundacion_calculado'] = (df['balance_hidrico'] * -1) + df['rango_termico']

    riesgo_inundacion = df['riesgo_inundacion_calculado'].mean()
    df['riesgo_sequia_calculado'] = df['balance_hidrico']
    riesgo_sequia = (df['riesgo_sequia_calculado'] < 0).mean()

    return {
        "riesgo_inundacion": round(riesgo_inundacion, 2),
        "riesgo_sequia": round(riesgo_sequia, 2)
    }

@app.get("/predict/cdmx")
def predict_cdmx():
    df = pd.read_csv(archivo_cdmx)
    resultado = calcular_riesgo(df)
    return {"estado": "CDMX", **resultado}

@app.get("/predict/edomex")
def predict_edomex():
    df = pd.read_csv(archivo_edomex)
    resultado = calcular_riesgo(df)
    return {"estado": "EDOMEX", **resultado}

# Ruta principal para verificar que la API funciona
@app.get("/")
def root():
    return {"message": "API de Inundaciones funcionando correctamente ✅"}