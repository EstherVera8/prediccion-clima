# Predicción de Riesgos Hidrometeorológicos: Inundación y Sequía

Este proyecto permite realizar predicciones simples sobre el **riesgo de inundación y sequía** en dos zonas:  
**CDMX** y **Estado de México**.  
Fue desarrollado como parte del proceso de **titulación de la carrera**.

---

## 🚀 Tecnologías utilizadas

- **Python**
- **Google Colab**
- **FastAPI**
- **Ngrok**
- **HTML / CSS (FrontEnd sencillo)**

---

## Estructura del Proyecto

proyecto-inundaciones/
├── conagua/
│ ├── CDMX.csv
│ └── ESTADO DE MÉXICO.csv
├── main.py
├── requirements.txt
└── EDOyCD.html
---

## Cómo ejecutar el proyecto

### Backend (API):
1. Abre Google Colab.
2. Conecta tu Drive donde están los archivos `.csv`.
3. Ejecuta `main.py` en Colab.
4. Expón el backend con `ngrok` para obtener tu URL.
5. Verifica que puedas acceder: `https://TU-URL-NGROK.ngrok-free.app/predict/cdmx`

### Frontend (Página Web):
1. Abre `EDOyCD.html` en tu navegador (puedes usar **Live Server** en VSCode).
2. Da clic en los botones **CDMX** o **EDO. MÉX.**
3. Consulta el resultado.

---

## Qué hace el proyecto

Este proyecto calcula un **índice de riesgo hídrico** a partir de los datos meteorológicos provistos en los archivos CSV:

- **Precipitación**
- **Evaporación**
- **Temperaturas máximas y mínimas**

Y devuelve un estimado sencillo de:
-  **Riesgo de Inundación**
-  **Riesgo de Sequía**

---

##  Objetivo académico
Este proyecto fue realizado como parte de mi **titulación profesional** para demostrar habilidades de:
- Programación en Python
- Análisis de datos meteorológicos
- Desarrollo de APIs
- Conexión Frontend - Backend

---

## Autor
**Esther Vera**  
[GitHub: EstherVera8](https://github.com/EstherVera8)

---

## Notas adicionales
- El proyecto es **educativo**, no científico.
- Los cálculos son aproximados y no deben usarse para decisiones oficiales.

---