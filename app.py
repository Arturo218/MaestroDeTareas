from flask import Flask, render_template, url_for, request, redirect  # Manejo de rutas y plantillas
from flask_sqlalchemy import SQLAlchemy  # Base de datos SQL
from datetime import datetime  # Manejo de fechas
from typing import List  # Tipado para listas

# Configuración de la aplicación Flask
app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db: SQLAlchemy = SQLAlchemy(app)

class Todo(db.Model):
    """
    Modelo de la base de datos para representar una tarea.
    """
    id: int = db.Column(db.Integer, primary_key=True)  # ID único para cada tarea
    content: str = db.Column(db.String(200), nullable=False)  # Contenido de la tarea
    date_created: datetime = db.Column(db.DateTime, default=datetime.utcnow)  # Fecha de creación
    observations: str = db.Column(db.String(200), nullable=False)  # Observaciones

    def __repr__(self) -> str:
        """
        Representación del modelo en formato string.
        """
        return f'<Task {self.id}>'


@app.route('/', methods=['POST', 'GET'])
def index() -> str:
    """
    Ruta principal de la aplicación. Permite listar y añadir tareas.

    Regresa:
        str: Renderizado de la plantilla index.html.
    """
    if request.method == 'POST':
        task_content: str = request.form['content']
        task_observations: str = request.form['observations']

        new_task: Todo = Todo(content=task_content, observations=task_observations)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'Hubo un problema al añadir su tarea'

    else:
        tasks: List[Todo] = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id: int) -> str:
    """
    Ruta para eliminar una tarea.

    Parámetros:
        id (int): ID de la tarea a eliminar.

    Regresa:
        str: Redirección a la ruta principal.
    """
    task_to_delete: Todo = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception:
        return 'Hubo un problema al borrar la tarea'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id: int) -> str:
    """
    Ruta para actualizar una tarea existente.

    Parámetros:
        id (int): ID de la tarea a actualizar.

    Regresa:
        str: Renderizado de la plantilla update.html o redirección a la ruta principal.
    """
    task: Todo = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        task.observations = request.form['observations']
        new_date_created: str = request.form['date_created']

        try:
            task.date_created = datetime.strptime(new_date_created, '%Y-%m-%dT%H:%M')
            db.session.commit()
            return redirect('/')
        except Exception:
            return 'Hubo un problema al actualizar la tarea'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    # Inicializa las tablas de la base de datos si no existen
    with app.app_context():
        db.create_all()  # Crear tablas en la base de datos
    app.run(debug=True)
    