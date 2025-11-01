# Smart Price Tracker

Una API y un scraper diseñados para monitorear los precios de productos en diferentes tiendas en línea. El objetivo es poder registrar productos a través de su URL y recibir alertas cuando sus precios cambien.

## ✨ Características Principales

- **API RESTful**: Endpoints para añadir y consultar productos monitoreados.
- **Scraper Web**: Módulo para extraer información de precios de páginas de productos.
- **Base de Datos**: (En desarrollo) Persistencia de datos usando PostgreSQL.
- **Esquemas de Datos**: Modelos de Pydantic para una validación de datos robusta.

## 🛠️ Tecnologías Utilizadas

- **Backend**: FastAPI
- **Scraping**: Requests & BeautifulSoup4
- **Servidor ASGI**: Uvicorn
- **Base de Datos**: PostgreSQL (planeado)
- **ORM**: SQLAlchemy (planeado)

## 🚀 Instalación y Puesta en Marcha

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/tu-usuario/smart-price-tracker.git
    cd smart-price-tracker
    ```

2.  **Crea un entorno virtual e instala las dependencias:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Ejecuta la API:**
    ```bash
    uvicorn api.main:app --reload
    ```
    La API estará disponible en `http://127.0.0.1:8000`.
