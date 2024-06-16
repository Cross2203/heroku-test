from sqlalchemy.orm import Session
from . import models, schemas

# Clientes CRUD
def get_clientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Cliente).offset(skip).limit(limit).all()

def get_cliente(db: Session, cliente_id: int):
    return db.query(models.Cliente).filter(models.Cliente.id_cliente == cliente_id).first()

def create_cliente(db: Session, cliente: schemas.ClienteCreate):
    db_cliente = models.Cliente(
        nombre=cliente.nombre,
        direccion=cliente.direccion,
        nombre_usuario=cliente.nombre_usuario,
        telefono=cliente.telefono,
        email=cliente.email,
        contrasena=cliente.contrasena,
        estado=cliente.estado
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def update_cliente(db: Session, cliente_id: int, cliente: schemas.ClienteCreate):
    db_cliente = get_cliente(db, cliente_id)
    if db_cliente:
        db_cliente.nombre = cliente.nombre
        db_cliente.direccion = cliente.direccion
        db_cliente.nombre_usuario = cliente.nombre_usuario
        db_cliente.telefono = cliente.telefono
        db_cliente.email = cliente.email
        db_cliente.contrasena = cliente.contrasena
        db_cliente.estado = cliente.estado
        db.commit()
        db.refresh(db_cliente)
    return db_cliente

def delete_cliente(db: Session, cliente_id: int):
    db_cliente = get_cliente(db, cliente_id)
    if db_cliente:
        db.delete(db_cliente)
        db.commit()
    return db_cliente

# Tipos de Alimentos CRUD
def get_tipos_alimentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.TipoAlimento).offset(skip).limit(limit).all()

def get_tipo_alimento(db: Session, tipo_id: int):
    return db.query(models.TipoAlimento).filter(models.TipoAlimento.id_tipo == tipo_id).first()

def create_tipo_alimento(db: Session, tipo: schemas.TipoAlimentoCreate):
    db_tipo = models.TipoAlimento(
        nombre_tipo=tipo.nombre_tipo
    )
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

def update_tipo_alimento(db: Session, tipo_id: int, tipo: schemas.TipoAlimentoCreate):
    db_tipo = get_tipo_alimento(db, tipo_id)
    if db_tipo:
        db_tipo.nombre_tipo = tipo.nombre_tipo
        db.commit()
        db.refresh(db_tipo)
    return db_tipo

def delete_tipo_alimento(db: Session, tipo_id: int):
    db_tipo = get_tipo_alimento(db, tipo_id)
    if db_tipo:
        db.delete(db_tipo)
        db.commit()
    return db_tipo

# Alimentos CRUD
def get_alimentos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Alimento).offset(skip).limit(limit).all()

def get_alimento(db: Session, alimento_id: int):
    return db.query(models.Alimento).filter(models.Alimento.id_alimento == alimento_id).first()

def create_alimento(db: Session, alimento: schemas.AlimentoCreate):
    db_alimento = models.Alimento(
        nombre=alimento.nombre,
        descripcion=alimento.descripcion,
        id_tipo=alimento.id_tipo
    )
    db.add(db_alimento)
    db.commit()
    db.refresh(db_alimento)
    return db_alimento

def update_alimento(db: Session, alimento_id: int, alimento: schemas.AlimentoCreate):
    db_alimento = get_alimento(db, alimento_id)
    if db_alimento:
        db_alimento.nombre = alimento.nombre
        db_alimento.descripcion = alimento.descripcion
        db_alimento.id_tipo = alimento.id_tipo
        db.commit()
        db.refresh(db_alimento)
    return db_alimento

def delete_alimento(db: Session, alimento_id: int):
    db_alimento = get_alimento(db, alimento_id)
    if db_alimento:
        db.delete(db_alimento)
        db.commit()
    return db_alimento

# Ordenes CRUD
def get_ordenes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Orden).offset(skip).limit(limit).all()

def get_orden(db: Session, orden_id: int):
    return db.query(models.Orden).filter(models.Orden.id_orden == orden_id).first()

def create_orden(db: Session, orden: schemas.OrdenCreate):
    db_orden = models.Orden(
        id_cliente=orden.id_cliente,
        id_estado=orden.id_estado,
        direccion_entrega=orden.direccion_entrega,
        total=orden.total,
        estado=orden.estado
    )
    db.add(db_orden)
    db.commit()
    db.refresh(db_orden)
    return db_orden

def update_orden(db: Session, orden_id: int, orden: schemas.OrdenCreate):
    db_orden = get_orden(db, orden_id)
    if db_orden:
        db_orden.id_cliente = orden.id_cliente
        db_orden.id_estado = orden.id_estado
        db_orden.direccion_entrega = orden.direccion_entrega
        db_orden.total = orden.total
        db_orden.estado = orden.estado
        db.commit()
        db.refresh(db_orden)
    return db_orden

def delete_orden(db: Session, orden_id: int):
    db_orden = get_orden(db, orden_id)
    if db_orden:
        db.delete(db_orden)
        db.commit()
    return db_orden

# Ordenes Detalles CRUD
def get_ordenes_detalles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.OrdenDetalle).offset(skip).limit(limit).all()

def get_orden_detalle(db: Session, orden_detalle_id: int):
    return db.query(models.OrdenDetalle).filter(models.OrdenDetalle.id_orden_detalle == orden_detalle_id).first()

def create_orden_detalle(db: Session, orden_detalle: schemas.OrdenDetalleCreate):
    db_orden_detalle = models.OrdenDetalle(
        id_orden=orden_detalle.id_orden,
        id_alimento=orden_detalle.id_alimento,
        id_estado=orden_detalle.id_estado,
        cantidad=orden_detalle.cantidad,
        precio_unitario=orden_detalle.precio_unitario,
        precio_total=orden_detalle.precio_total
    )
    db.add(db_orden_detalle)
    db.commit()
    db.refresh(db_orden_detalle)
    return db_orden_detalle

def update_orden_detalle(db: Session, orden_detalle_id: int, orden_detalle: schemas.OrdenDetalleCreate):
    db_orden_detalle = get_orden_detalle(db, orden_detalle_id)
    if db_orden_detalle:
        db_orden_detalle.id_orden = orden_detalle.id_orden
        db_orden_detalle.id_alimento = orden_detalle.id_alimento
        db_orden_detalle.id_estado = orden_detalle.id_estado
        db_orden_detalle.cantidad = orden_detalle.cantidad
        db_orden_detalle.precio_unitario = orden_detalle.precio_unitario
        db_orden_detalle.precio_total = orden_detalle.precio_total
        db.commit()
        db.refresh(db_orden_detalle)
    return db_orden_detalle

def delete_orden_detalle(db: Session, orden_detalle_id: int):
    db_orden_detalle = get_orden_detalle(db, orden_detalle_id)
    if db_orden_detalle:
        db.delete(db_orden_detalle)
        db.commit()
    return db_orden_detalle

def read_ultima_orden(db: Session):
    return db.query(models.Orden).order_by(models.Orden.fecha.desc()).first()

def create_estado_ordenes(db: Session, estado_ordenes: schemas.EstadoOrdenCreate):
    db_estado_orden = models.EstadoOrden(**estado_ordenes.model_dump())
    db.add(db_estado_orden)
    db.commit()
    db.refresh(db_estado_orden)
    return db_estado_orden

def get_estado_ordenes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.EstadoOrden).offset(skip).limit(limit).all()

def get_estado_orden(db: Session, estado_orden_id: int):
    return db.query(models.EstadoOrden).filter(models.EstadoOrden.id_estado == estado_orden_id).first()

def update_estado_ordenes(db: Session, estado_ordenes_id: int, estado_ordenes: schemas.EstadoOrdenCreate):
    db_estado_orden = get_estado_orden(db, estado_ordenes_id)
    if db_estado_orden:
        for key, value in estado_ordenes.model_dump().items():
            setattr(db_estado_orden, key, value)
        db.commit()
        db.refresh(db_estado_orden)
    return db_estado_orden

def delete_estado_ordenes(db: Session, estado_ordenes_id: int):
    db_estado_orden = get_estado_orden(db, estado_ordenes_id)
    if db_estado_orden:
        db.delete(db_estado_orden)
        db.commit()
    return db_estado_orden

def update_ultima_orden(db: Session, orden: schemas.OrdenCreate):
    ultima_orden = db.query(models.Orden).order_by(models.Orden.fecha.desc()).first()
    if ultima_orden:
        for key, value in orden.model_dump().items():
            setattr(ultima_orden, key, value)
        db.commit()
        db.refresh(ultima_orden)
    return ultima_orden