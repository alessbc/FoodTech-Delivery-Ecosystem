# 🍔 Cloud Kitchen Hub: Ecosistema Food-Tech (Reto de Negocio)

Solución tecnológica integral diseñada para el control de márgenes de rentabilidad, automatización de inventarios y análisis de ventas en aplicaciones de delivery para el modelo de negocio *Dark Kitchens*.

**Nota sobre Integración Académica:** Este repositorio contiene un ecosistema de software completo (*End-to-End*) que da respuesta simultánea a dos entregables de ingeniería:
1. **Taller 13 (Taller Final):** Evaluación de la arquitectura Backend relacional (SQLite), manipulación de datos vía Python y el desarrollo de un Frontend transaccional y blindado en Tkinter.
2. **Taller 12:** Evaluación de la capa de Inteligencia de Negocios (Power BI), modelado de métricas avanzadas (DAX), UI/UX y la resolución de preguntas corporativas directas.

Al unificar ambos talleres en un solo repositorio, demostramos la capacidad de escalar un sistema operativo hacia una herramienta de analítica gerencial sin fragmentar el código.

## 👥 Equipo de Ingeniería y Arquitectura
* **Maria Jose Huertas** (Dirección de Proyecto e Integración de Backend SQLite)
* **Alessandro Di-Mauro Bonilla Correa** (Lógica de Interfaz Tkinter e Ingeniería de Datos)
* **Gabriela Ruiz** (Modelado Analítico DAX, Inteligencia de Negocios y Diseño UI/UX)

## 🏗️ Estructura Técnica Operativa (Taller 13)
* **Capa Backend (`database.py`):** Motor relacional SQLite estructurado bajo Modelo Estrella. Ejecuta un *Data Seeding* de 5 registros mínimos por tabla de manera autónoma al iniciar el orquestador.
* **Capa Frontend (`app_foodtech.py`):** GUI desarrollada en `Tkinter` con controles CRUD funcionales y estética Dark Mode tecnológica. Implementa manejo de excepciones de usuario con `try-except`.
* **Ejecución:** Archivo orquestador `main.py` ubicado en la raíz.

## 📊 Analítica y Business Intelligence (Taller 12)
* **Extracción Robusta (`FoodTech_Dashboard.pbix`):** Conectado a la bóveda relacional a través de un script puente nativo de Python (`pandas`), asegurando portabilidad en entornos de despliegue externos.
* **Modelado Analítico:** Uso extensivo de funciones DAX (`DIVIDE`, `SUM`, `CALCULATE`), Inteligencia de Tiempo mediante Tabla Calendario y Columnas Calculadas.
* **Toma de Decisiones:** Tablero diseñado bajo la regla de los 5 segundos con paleta Dark Tech. Incluye una pestaña de **Q&A** que documenta analíticamente la viabilidad financiera de las cocinas.

## 🚀 Despliegue Local
1. Clonar el repositorio.
2. Ejecutar `python main.py` para activar la interfaz de ventas y crear la base de datos automáticamente.
3. Operar los botones CRUD para ingresar transacciones a la red.
4. Abrir Power BI, dirigirse a *Transformar Datos* y modificar la variable `ruta_db` en el origen del script de Python para establecer la conexión local en vivo. Hacer clic en **Actualizar** para visualizar el impacto de las nuevas ventas.
