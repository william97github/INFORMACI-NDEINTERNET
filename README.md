# API REST CON FLASK Y MYSQL

No logre hacer una imagen del proyecto en Dockerfile 

Instalar dependencias

```bash
    pip install -r requeriments.txt
```

Credenciales .env

```bash
    SECRET_KEY="mysecret"
    FLASK_APP=main.py
    FLASK_DEBUG=1
    FLASK_ENV=FLASK_DEVELOPMENT
    SQLALCHEMY_DATABASE_URI= mysql://root:1234@localhost/flaskproyecto
```

Cambiar la ruta del archivo excel main.py

```bash
    ubicacion = 'C:\\Users\\william\\PycharmProjects\\miproyecto\\flask.xlsx'
```

La lectura y carga del archivo flask.xlsx se realiza en automatico al ingresar a la ruta raiz 

```bash
    http://127.0.0.1:5000/
```

Metodos GET API REST

```bash
    http://127.0.0.1:5000/ver-sedes
    http://127.0.0.1:5000/ver-departamentos-empresas
    http://127.0.0.1:5000/ver-empresas
    http://127.0.0.1:5000/ver-empresas-tecnologias-velocidades
```

