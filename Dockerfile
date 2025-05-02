# Usamos una imagen base ligera de Python 3.10
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de dependencias al contenedor
COPY requirements.txt .

# Instalamos las dependencias definidas en requirements.txt sin guardar caché (para mantener la imagen ligera)
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos los archivos principales de la aplicación al directorio de trabajo en el contenedor
COPY app.py predictor.py .

# Copiamos la carpeta de plantillas HTML (para renderizar vistas con Flask)
COPY templates/ templates/

# Copiamos la carpeta de archivos estáticos (CSS, imágenes, JS, etc.)
COPY static/ static/

# Exponemos el puerto 5000 para que pueda ser accedido desde fuera del contenedor
EXPOSE 5000

# Definimos el comando que se ejecutará al iniciar el contenedor
CMD ["python", "app.py"]
