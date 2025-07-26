✅ README.md proyecto "LibroBlog"

# 📚 LibroBlog

**LibroBlog** es una aplicación web desarrollada con Django que permite a los usuarios crear, ver, editar y eliminar reseñas de libros. Además, cuenta con funcionalidades de autenticación, perfiles de usuario y mensajería interna entre usuarios registrados.

---

## 🚀 Funcionalidades

- Página de inicio con presentacion del proyecto
- Página "Acerca de mí"
- Listado de libros
- Vista de detalle por cada libro
- Crear, editar y borrar reseñas (solo si estás logueado)
- Registro, login y logout de usuarios
- Envío de mensajes entre usuarios
- Manejo de imágenes en reseñas y perfiles

---

## 🛠 Tecnologías utilizadas

- Python 3.x
- Django 4.x
- SQLite (base de datos por defecto)
- HTML5 / CSS3
- Bootstrap
- Pillow (para manejo de imágenes)
- CKEditor (para texto enriquecido)
- Django Class-Based Views (CBV) y mixins

---

## ⚙️ Instalación y ejecución local

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/libroblog.git
cd libroblog

2. **Crear entorno virtual e instalar dependencias**

python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt

3. **Realizar migraciones**

python manage.py makemigrations
python manage.py migrate

4. **Crear un superusuario (opcional para acceder al admin)**

python manage.py createsuperuser

5. **Correr el servidor**

python manage.py runserver
Acceder desde: http://localhost:8000

📁 Estructura general del proyecto
books/ – App principal de reseñas

accounts/ – App para autenticación y perfiles de usuario

messaging/ – App para mensajes internos

media/ – Carpeta de archivos subidos (imágenes)

static/ – Archivos estáticos (CSS, imágenes propias del sitio)

templates/ – Templates HTML con herencia

db.sqlite3 – NO incluida en el repositorio

🔒 Importante
Este repositorio no incluye:

db.sqlite3 (por seguridad y limpieza del repositorio)

Carpeta media/ (por tamaño)

Datos precargados (la app se construye con migraciones)

🧾 Requisitos del proyecto
✅ Uso de CBVs
✅ Uso de mixin y decorador
✅ Herencia de templates
✅ Modelo principal Libro con 2 CharFields, 1 campo enriquecido (ckeditor), 1 imagen, 1 fecha
✅ Rutas /about/, /pages/, /pages/<id>/
✅ CRUD completo para libros
✅ Login, logout, registro
✅ Perfil de usuario editable
✅ Mensajería entre usuarios
✅ Mensaje "No hay reseñas aún" si está vacío

📹 Demo
👉 Video de presentación: https://drive.google.com/file/d/17DbkwZQU-Y5QojjllHvXLRTtbM4Ggbyo/view?usp=sharing

🧑‍💻 Autor
Nombre y apellido: Florencia Marcat
Curso:Coder House- python flex  Proyecto pagina web con Django
Contacto: flormarc22@gmail.com

📝 Licencia
Este proyecto se entrega como parte de una evaluación educativa. Uso académico solamente.
