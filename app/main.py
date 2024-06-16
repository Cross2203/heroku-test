from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Clientes Endpoints
@app.post("/clientes/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db=db, cliente=cliente)

@app.get("/clientes/", response_model=List[schemas.Cliente])
def read_clientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_clientes(db, skip=skip, limit=limit)

@app.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente(db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    return db_cliente

@app.put("/clientes/{cliente_id}", response_model=schemas.Cliente)
def update_cliente(cliente_id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.update_cliente(db, cliente_id, cliente)

@app.delete("/clientes/{cliente_id}", response_model=schemas.Cliente)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return crud.delete_cliente(db, cliente_id)

# Tipos de Alimentos Endpoints
@app.post("/tipos_alimentos/", response_model=schemas.TipoAlimento)
def create_tipo_alimento(tipo: schemas.TipoAlimentoCreate, db: Session = Depends(get_db)):
    return crud.create_tipo_alimento(db=db, tipo=tipo)

@app.get("/tipos_alimentos/", response_model=List[schemas.TipoAlimento])
def read_tipos_alimentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_tipos_alimentos(db, skip=skip, limit=limit)

@app.get("/tipos_alimentos/{tipo_id}", response_model=schemas.TipoAlimento)
def read_tipo_alimento(tipo_id: int, db: Session = Depends(get_db)):
    db_tipo = crud.get_tipo_alimento(db, tipo_id=tipo_id)
    if db_tipo is None:
        raise HTTPException(status_code=404, detail="Tipo de Alimento not found")
    return db_tipo

@app.put("/tipos_alimentos/{tipo_id}", response_model=schemas.TipoAlimento)
def update_tipo_alimento(tipo_id: int, tipo: schemas.TipoAlimentoCreate, db: Session = Depends(get_db)):
    return crud.update_tipo_alimento(db, tipo_id, tipo)

@app.delete("/tipos_alimentos/{tipo_id}", response_model=schemas.TipoAlimento)
def delete_tipo_alimento(tipo_id: int, db: Session = Depends(get_db)):
    return crud.delete_tipo_alimento(db, tipo_id)


@app.post("/alimentos/", response_model=schemas.Alimento)
def create_alimento(alimento: schemas.AlimentoCreate, db: Session = Depends(get_db)):
    return crud.create_alimento(db=db, alimento=alimento)

@app.get("/alimentos/", response_model=List[schemas.Alimento])
def read_alimentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_alimentos(db, skip=skip, limit=limit)

@app.get("/alimentos/{alimento_id}", response_model=schemas.Alimento)
def read_alimento(alimento_id: int, db: Session = Depends(get_db)):
    db_alimento = crud.get_alimento(db, alimento_id=alimento_id)
    if db_alimento is None:
        raise HTTPException(status_code=404, detail="Alimento not found")
    return db_alimento

@app.put("/alimentos/{alimento_id}", response_model=schemas.Alimento)
def update_alimento(alimento_id: int, alimento: schemas.AlimentoCreate, db: Session = Depends(get_db)):
    return crud.update_alimento(db, alimento_id, alimento)

@app.delete("/alimentos/{alimento_id}", response_model=schemas.Alimento)
def delete_alimento(alimento_id: int, db: Session = Depends(get_db)):
    return crud.delete_alimento(db, alimento_id)

@app.post("/estado_ordenes/", response_model=schemas.EstadoOrden)
def create_estado_ordenes(estado_ordenes: schemas.EstadoOrdenCreate, db: Session = Depends(get_db)):
    return crud.create_estado_ordenes(db=db, estado_ordenes=estado_ordenes)

@app.get("/estado_ordenes/", response_model=List[schemas.EstadoOrden])
def read_estado_ordenes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_estado_ordenes(db, skip=skip, limit=limit)

@app.get("/estado_ordenes/{estado_ordenes_id}", response_model=schemas.EstadoOrden)
def read_estado_orden(estado_orden_id: int, db: Session = Depends(get_db)):
    db_estado_orden = crud.get_estado_ordes(db, estado_orden_id=estado_orden_id)
    if db_estado_orden is None:
        raise HTTPException(status_code=404, detail="EstadoOrden not found")
    return db_estado_orden

@app.put("/estado_ordenes/{estado_ordenes_id}", response_model=schemas.EstadoOrden)
def update_estado_ordenes(estado_ordenes_id: int, estado_ordenes: schemas.EstadoOrdenCreate, db: Session = Depends(get_db)):
    return crud.update_estado_ordenes(db, estado_ordenes_id, estado_ordenes)

@app.delete("/estado_ordenes/{estado_ordenes_id}", response_model=schemas.EstadoOrden)
def delete_estado_ordenes(estado_ordenes_id: int, db: Session = Depends(get_db)):
    return crud.delete_estado_ordenes(db, estado_ordenes_id)

@app.post("/ordenes/", response_model=schemas.Orden)
def create_orden(orden: schemas.OrdenCreate, db: Session = Depends(get_db)):
    return crud.create_orden(db=db, orden=orden)

@app.get("/ordenes/", response_model=List[schemas.Orden])
def read_ordenes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_ordenes(db, skip=skip, limit=limit)

@app.get("/ordenes/{orden_id}", response_model=schemas.Orden)
def read_orden(orden_id: int, db: Session = Depends(get_db)):
    db_orden = crud.get_orden(db, orden_id=orden_id)
    if db_orden is None:
        raise HTTPException(status_code=404, detail="Orden not found")
    return db_orden

@app.put("/ordenes/{orden_id}", response_model=schemas.Orden)
def update_orden(orden_id: int, orden: schemas.OrdenCreate, db: Session = Depends(get_db)):
    return crud.update_orden(db, orden_id, orden)

@app.delete("/ordenes/{orden_id}", response_model=schemas.Orden)
def delete_orden(orden_id: int, db: Session = Depends(get_db)):
    return crud.delete_orden(db, orden_id)

# Ordenes Detalles Endpoints
@app.post("/ordenes_detalles/", response_model=schemas.OrdenDetalle)
def create_orden_detalle(orden_detalle: schemas.OrdenDetalleCreate, db: Session = Depends(get_db)):
    return crud.create_orden_detalle(db=db, orden_detalle=orden_detalle)

@app.get("/ordenes_detalles/", response_model=List[schemas.OrdenDetalle])
def read_ordenes_detalles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_ordenes_detalles(db, skip=skip, limit=limit)

@app.get("/ordenes_detalles/{orden_detalle_id}", response_model=schemas.OrdenDetalle)
def read_orden_detalle(orden_detalle_id: int, db: Session = Depends(get_db)):
    db_orden_detalle = crud.get_orden_detalle(db, orden_detalle_id=orden_detalle_id)
    if db_orden_detalle is None:
        raise HTTPException(status_code=404, detail="Orden Detalle not found")
    return db_orden_detalle

@app.put("/ordenes_detalles/{orden_detalle_id}", response_model=schemas.OrdenDetalle)
def update_orden_detalle(orden_detalle_id: int, orden_detalle: schemas.OrdenDetalleCreate, db: Session = Depends(get_db)):
    return crud.update_orden_detalle(db, orden_detalle_id, orden_detalle)

@app.delete("/ordenes_detalles/{orden_detalle_id}", response_model=schemas.OrdenDetalle)
def delete_orden_detalle(orden_detalle_id: int, db: Session = Depends(get_db)):
    return crud.delete_orden_detalle(db, orden_detalle_id)
