# Usamos la imagen base de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido de la aplicación al contenedor
COPY . .

# Exponemos el puerto 5001
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["python","app.py"]                               