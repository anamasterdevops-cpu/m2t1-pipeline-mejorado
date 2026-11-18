# Imagen base: Alpine Linux 3.24 (la misma que en la Tarea 2)
FROM alpine:3.24

# Instalamos Python 3 sin guardar la caché de apk para que la imagen pese menos.
# Fijamos la versión exacta (aviso DL3018 de hadolint) para que la imagen sea reproducible.
RUN apk add --no-cache python3=3.14.10-r1

# Creamos un usuario sin privilegios (UID y GID 10001) para no ejecutar la aplicación como root
RUN addgroup -S -g 10001 calculadora && adduser -S -u 10001 -G calculadora calculadora

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos solo lo necesario para ejecutar la calculadora (no los tests ni el pipeline)
COPY calculadora.py .

# Variables de entorno por defecto (se pueden cambiar con docker run -e)
ENV OPERACION=multiplicacion NUM1=6 NUM2=7

# A partir de aquí todo se ejecuta con el usuario sin privilegios.
# Usamos el UID numérico (aviso DL3066 de hadolint) para que se resuelva igual en cualquier sistema.
USER 10001

# Comando que se ejecuta al arrancar el contenedor
CMD ["python3", "calculadora.py"]
