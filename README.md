# Maestro de Tareas

Una aplicación web sencilla desarrollada con **Python**, **Flask** y **SQLite3** que permite a los usuarios gestionar tareas. Incluye funcionalidades para agregar, actualizar y eliminar tareas.

---

## Características

- **Agregar tareas**: Permite al usuario registrar nuevas tareas con una fecha de creación automática.
- **Actualizar tareas**: Modifica el contenido de una tarea y actualiza su fecha de creación.
- **Eliminar tareas**: Elimina tareas específicas de la lista.
- **Visualización en tabla**: Muestra las tareas en un formato tabular con acciones disponibles.

---

## Tecnologías utilizadas

### **Lenguaje principal**
- [Python](https://www.python.org): Para la lógica de backend.

### **Framework web**
- [Flask](https://flask.palletsprojects.com): Para el desarrollo de la aplicación web.

### **Base de datos**
- [SQLite3](https://www.sqlite.org): Para almacenamiento de datos local.

### **Frontend**
- HTML, CSS (estilo sencillo definido en el archivo `main.css`).

---

## Instalación y configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Arturo218/MaestroDeTareas.git
   cd MaestroDeTareas

Utilizando una terminal realiza los siguientes pasos:

-Crea un entorno virtual:
python -m venv env
source env/bin/activate  # En Windows: .\env\Scripts\activate

-Instala las dependencias desde la termina:
pip install -r requirements.txt

Ejecuta la aplicación:
python app.py
Abre un navegador web e ingresa a http://127.0.0.1:5000 para acceder a la aplicación Web.