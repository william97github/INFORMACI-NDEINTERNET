from app.db import db

class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(50), nullable=False)
    detalles = db.relationship('Detalle', backref='estado', lazy=True)
    def __init__(self, estado):
        self.estado = estado

class Departamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(50), nullable=False)
    detalles = db.relationship('Detalle', backref='departamento', lazy=True)
    def __init__(self, departamento):
        self.departamento = departamento

class Segmento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    segmento = db.Column(db.String(50), nullable=False)
    detalles = db.relationship('Detalle', backref='segmento', lazy=True)
    def __init__(self, segmento):
        self.segmento = segmento

class Tecnologia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tecnologia = db.Column(db.String(50), nullable=False)
    detalles = db.relationship('Detalle', backref='tecnologia', lazy=True)
    def __init__(self, tecnologia):
        self.tecnologia = tecnologia

class Velocidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    velocidad = db.Column(db.String(50), nullable=False)
    detalles = db.relationship('Detalle', backref='velocidad', lazy=True)
    def __init__(self, velocidad):
        self.velocidad = velocidad

class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ruc = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    detalles = db.relationship('Detalle', backref='empresa', lazy=True)
    def __init__(self, ruc, nombre):
        self.ruc = ruc
        self.nombre = nombre

class Detalle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id'), nullable=False)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'), nullable=False)
    departamento_id = db.Column(db.Integer, db.ForeignKey('departamento.id'), nullable=False)
    segmento_id = db.Column(db.Integer, db.ForeignKey('segmento.id'), nullable=False)
    tecnologia_id = db.Column(db.Integer, db.ForeignKey('tecnologia.id'), nullable=False)
    velocidad_id = db.Column(db.Integer, db.ForeignKey('velocidad.id'), nullable=False)
    def __init__(self, empresa_id, estado_id, departamento_id, segmento_id, tecnologia_id, velocidad_id):
        self.empresa_id = empresa_id
        self.estado_id = estado_id
        self.departamento_id = departamento_id
        self.segmento_id = segmento_id
        self.tecnologia_id = tecnologia_id
        self.velocidad_id = velocidad_id