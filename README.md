# Sistema de Predicción Hidrométrica CDMX y EDOMEX

Este proyecto predice el riesgo de **inundación** y **sequía** en la **Ciudad de México** y **Estado de México** utilizando datos meteorológicos de CONAGUA.

Fue desarrollado con:
- **FastAPI** (Backend)
- **HTML + CSS + JavaScript** (Frontend)
- **Pandas** (Análisis de datos)

---

## ¿Cómo ejecutar?

1️ Instalar dependencias:
```bash
pip install fastapi uvicorn pandas
```

2️ Ejecutar el servidor:
```bash
uvicorn main:app --reload
```

3️ Acceder en navegador:
- API: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Interfaz Web: abrir `web/index.html` manualmente desde el navegador.

---

## Estructura del Proyecto
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

## Funcionalidades
- Predicción de riesgo de **inundación** y **sequía**.
- Visualización de resultados por estado.
- Mapas, patrones climáticos y explicación del proceso.

---

## Proyecto.
Este proyecto fue realizado como parte de mi **titulación profesional** para demostrar habilidades de:

- Desarrollo Backend

    - Uso de FastAPI para crear servicios RESTful.
    - Creación de rutas HTTP para consumo de datos.
    - Manejo de frameworks modernos de Python.

- Programación en Python
    - Manipulación de datos con pandas.
    - Lógica para cálculos matemáticos e interpretación de datos climatológicos.
    - Buenas prácticas de organización de código.

- Desarrollo Frontend Básico
    - Creación de páginas web estáticas usando HTML, CSS y JavaScript.
    - Diseño de interfaz sencilla, limpia y funcional.
    - Implementación de menús y navegación.

- Integración Backend + Frontend
    - Comunicación entre el servidor FastAPI y la página web.
    - Diseño de un flujo completo para que el usuario pueda consultar predicciones de forma amigable.

- Visualización y Análisis de Datos
    - Aplicación de análisis básico de datos meteorológicos.
    - Interpretación de información para generar resultados comprensibles.
    - Visualización de resultados mediante mapas e interfaces.

- Estructuración de Proyectos
    - Organización de carpetas y archivos de un proyecto profesional.
    - Documentación clara (README.md, PDF explicativo).

- Herramientas y Entornos
    - Manejo de PowerShell, Visual Studio Code.
    - Comprensión de entornos virtuales y dependencias.
    - Conocimientos básicos de despliegue local.

---

- Habilidades Académicas
    - Redacción técnica y explicación de procesos.
    - Capacidad para estructurar proyectos con fines académicos.
    - Comunicación visual de datos y resultados.
    
---

## Autor
**Esther Vera**  
[GitHub: EstherVera8](https://github.com/EstherVera8)

---

## Notas adicionales
- El proyecto es **educativo**, no científico.
- Los cálculos son aproximados y no deben usarse para decisiones oficiales.

---
