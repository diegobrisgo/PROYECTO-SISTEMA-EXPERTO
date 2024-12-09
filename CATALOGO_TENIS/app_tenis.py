from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Configuración inicial
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogo_tenis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Carpeta para guardar imágenes

# Asegúrate de que la carpeta de uploads existe
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

db = SQLAlchemy(app)

# Modelo para la base de datos
class Tenis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    talla = db.Column(db.Float, nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    disponibilidad = db.Column(db.String(50), nullable=False)
    imagen = db.Column(db.String(200), nullable=True)  # Ruta de la imagen

# Ruta para la página principal con filtros
@app.route('/')
def index():
    # Capturar parámetros de filtro desde la URL
    genero = request.args.get('genero')
    talla = request.args.get('talla')
    disponibilidad = request.args.get('disponibilidad')

    # Crear consulta base
    query = Tenis.query

    # Aplicar filtros según los parámetros
    if genero:
        query = query.filter_by(genero=genero)
    if talla:
        query = query.filter_by(talla=float(talla))
    if disponibilidad:
        query = query.filter_by(disponibilidad=disponibilidad)

    # Obtener resultados filtrados
    tenis = query.all()
    return render_template('index.html', tenis=tenis)

# Ruta para agregar tenis
@app.route('/add', methods=['GET', 'POST'])
def add_tenis():
    if request.method == 'POST':
        nombre = request.form['nombre']
        talla = request.form['talla']
        genero = request.form['genero']
        disponibilidad = request.form['disponibilidad']

        # Manejo del archivo de imagen
        imagen_file = request.files['imagen']
        if imagen_file:
            imagen_path = os.path.join(app.config['UPLOAD_FOLDER'], imagen_file.filename)
            imagen_file.save(imagen_path)
        else:
            imagen_path = None

        # Guardar en la base de datos
        nuevo_tenis = Tenis(
            nombre=nombre,
            talla=float(talla),
            genero=genero,
            disponibilidad=disponibilidad,
            imagen=imagen_path
        )
        db.session.add(nuevo_tenis)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add.html')

# Ruta para editar un tenis
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_tenis(id):
    tenis = Tenis.query.get_or_404(id)  # Obtener el producto por su ID o devolver un error 404

    if request.method == 'POST':
        # Actualizar los campos con los datos del formulario
        tenis.nombre = request.form['nombre']
        tenis.talla = request.form['talla']
        tenis.genero = request.form['genero']
        tenis.disponibilidad = request.form['disponibilidad']

        # Manejo del archivo de imagen
        imagen_file = request.files['imagen']
        if imagen_file:
            imagen_path = os.path.join(app.config['UPLOAD_FOLDER'], imagen_file.filename)
            imagen_file.save(imagen_path)
            tenis.imagen = imagen_path  # Actualizar la ruta de la imagen

        db.session.commit()  # Guardar los cambios en la base de datos
        return redirect(url_for('index'))

    return render_template('edit.html', tenis=tenis)  # Mostrar formulario prellenado


# Inicializar la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
