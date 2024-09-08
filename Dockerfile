# Utilizar una imagen base de Python más nueva
FROM python:3.11-slim

# Instalar dependencias del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos y el código fuente
COPY requirements.txt /app/
COPY src/ /app/

# Instalar las dependencias con un tiempo de espera aumentado
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements.txt

# Exponer el puerto en el que correrá la API
EXPOSE 5000

# Comando para correr la aplicación
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]
