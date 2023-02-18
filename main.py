from app import create_app
from app.db import db
from flask_marshmallow import Marshmallow
from app.models.modelos import Estado, Departamento, Segmento, Tecnologia, Velocidad, Empresa, Detalle
from flask import render_template
import xlrd
import json


app=create_app()
ma = Marshmallow(app)

class EstadoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'estado')
        model = Estado
estado_schema = EstadoSchema()
estado_schema = EstadoSchema(many=True)

class DepartamentoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'departamento')
        model = Departamento
departamento_schema = DepartamentoSchema()
departamento_schema = DepartamentoSchema(many=True)

class SegmentoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'segmento')
        model = Segmento
segmento_schema = SegmentoSchema()
segmento_schema = SegmentoSchema(many=True)

class TecnologiaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'tecnologia')
        model = Tecnologia
tecnologia_schema = TecnologiaSchema()
tecnologia_schema = TecnologiaSchema(many=True)

class VelocidadSchema(ma.Schema):
    class Meta:
        fields = ('id', 'velocidad')
        model = Velocidad
velocidad_schema = VelocidadSchema()
velocidad_schema = VelocidadSchema(many=True)

class EmpresaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'ruc', 'nombre')
        model = Empresa
empresa_schema = EmpresaSchema()
empresa_schema = EmpresaSchema(many=True)

class DetalleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'empresa_id', 'estado_id', 'departamento_id', 'segmento_id', 'tecnologia_id', 'velocidad_id')
        model = Detalle
detalle_schema = DetalleSchema()
detalle_schema = DetalleSchema(many=True)


@app.route('/ver-sedes', methods = ['GET'])
def listar_sedes():
    resultado = db.engine.execute('select * from Departamento;')
    return departamento_schema.dump(resultado)

@app.route('/ver-departamentos-empresas', methods = ['GET'])
def listar_departamentos_empresas():
    resultado = db.engine.execute('SELECT departamento, nombre from detalle inner join departamento on detalle.departamento_id=departamento.id inner join empresa on detalle.empresa_id=empresa.id;')
    return json.dumps([dict(r) for r in resultado])

@app.route('/ver-empresas', methods = ['GET'])
def listar_empresas():
    resultado = db.engine.execute('select * from Empresa;')
    return empresa_schema.dump(resultado)

@app.route('/ver-empresas-tecnologias-velocidades', methods = ['GET'])
def listar_empresas_tecnologias_velocidades():
    resultado = db.engine.execute('SELECT nombre, tecnologia, velocidad from detalle inner join tecnologia on detalle.tecnologia_id=tecnologia.id inner join velocidad on detalle.velocidad_id=velocidad.id inner join empresa on detalle.empresa_id=empresa.id;')
    return json.dumps([dict(r) for r in resultado])


ubicacion = 'C:\\Users\\william\\PycharmProjects\\miproyecto\\flask.xlsx'
abrir = xlrd.open_workbook(ubicacion)

@app.route('/',)
def index():
    hoja1 = abrir.sheet_by_name("Hoja1")
    for i in range(hoja1.nrows):
        dato1 = hoja1.cell_value(i, 0)
        nuevo = Estado(dato1)
        db.session.add(nuevo)
        db.session.commit()

    hoja2 = abrir.sheet_by_name("Hoja2")
    for i in range(hoja2.nrows):
        dato1 = hoja2.cell_value(i, 0)
        nuevo = Departamento(dato1)
        db.session.add(nuevo)
        db.session.commit()

    hoja3 = abrir.sheet_by_name("Hoja3")
    for i in range(hoja3.nrows):
        dato1 = hoja3.cell_value(i, 0)
        nuevo = Tecnologia(dato1)
        db.session.add(nuevo)
        db.session.commit()

    hoja4 = abrir.sheet_by_name("Hoja4")
    for i in range(hoja4.nrows):
        dato1 = hoja4.cell_value(i, 0)
        nuevo = Velocidad(dato1)
        db.session.add(nuevo)
        db.session.commit()

    hoja5 = abrir.sheet_by_name("Hoja5")
    for i in range(hoja5.nrows):
        dato1 = hoja5.cell_value(i, 0)
        nuevo = Segmento(dato1)
        db.session.add(nuevo)
        db.session.commit()

    hoja6 = abrir.sheet_by_name("Hoja6")
    for i in range(hoja6.nrows):
        dato1 = hoja6.cell_value(i, 0)
        dato2 = hoja6.cell_value(i, 1)
        nuevo = Empresa(dato1, dato2)
        db.session.add(nuevo)
        db.session.commit()

    hoja7 = abrir.sheet_by_name("Hoja7")
    for i in range(hoja7.nrows):
        dato1 = hoja7.cell_value(i, 0)
        dato2 = hoja7.cell_value(i, 1)
        dato3 = hoja7.cell_value(i, 2)
        dato4 = hoja7.cell_value(i, 3)
        dato5 = hoja7.cell_value(i, 4)
        dato6 = hoja7.cell_value(i, 5)
        nuevo = Detalle(dato1, dato2, dato3, dato4, dato5, dato6)
        db.session.add(nuevo)
        db.session.commit()

    resultados = Empresa.query.all()
    return render_template('index.html', resultados= resultados)



db.init_app(app)
with app.app_context():
    db.create_all()
    print("BD conectada!")

if __name__ == "__main__":
    app.run(debug=True)
