#  Sistema de Predicción Hidrométrica CDMX y EDOMEX

Este proyecto predice el riesgo de **inundación** y **sequía** en la **Ciudad de México** y **Estado de México** utilizando datos meteorológicos de CONAGUA.

Fue desarrollado con:
- ⚙️ **FastAPI** (Backend)
- 🎨 **HTML + CSS + JavaScript** (Frontend)
- 📈 **Pandas** (Análisis de datos)

---

## 🚀 ¿Cómo ejecutar?

1️⃣ Instalar dependencias:
```bash
pip install fastapi uvicorn pandas
```

2️⃣ Ejecutar el servidor:
```bash
uvicorn main:app --reload
```

3️⃣ Acceder en navegador:
- API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Interfaz Web: abrir `web/index.html` manualmente desde el navegador.

---

## 📂 Estructura del Proyecto
```
proyecto-inundaciones/
├── main.py
├── conagua/
│   ├── CDMX.csv
│   ├── ESTADO DE MEXICO.csv
├── web/
│   ├── index.html
│   ├── mapa_cdmx.png
│   ├── mapa_edomex.png
├── README.md
```

---

## 📌 Funcionalidades
- Predicción de riesgo de **inundación** y **sequía**.
- Visualización de resultados por estado.
- Mapas, patrones climáticos y explicación del proceso.

---

## Proyecto.
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
