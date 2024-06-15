from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ClienteBase(BaseModel):
    nombre: str
    direccion: str
    nombre_usuario: str
    telefono: Optional[str]
    email: str
    estado: Optional[str]

class ClienteCreate(ClienteBase):
    contrasena: str

class Cliente(ClienteBase):
    id_cliente: int

    class Config:
        orm_mode = True

class TipoAlimentoBase(BaseModel):
    nombre_tipo: str

class TipoAlimentoCreate(TipoAlimentoBase):
    pass

class TipoAlimento(TipoAlimentoBase):
    id_tipo: int

    class Config:
        orm_mode = True

class AlimentoBase(BaseModel):
    nombre: str
    descripcion: str
    id_tipo: int

class AlimentoCreate(AlimentoBase):
    pass

class Alimento(AlimentoBase):
    id_alimento: int

    class Config:
        orm_mode = True

class EstadoOrdenBase(BaseModel):
    nombre_estado: str

class EstadoOrdenCreate(EstadoOrdenBase):
    pass

class EstadoOrden(EstadoOrdenBase):
    id_estado: int

    class Config:
        orm_mode = True

class OrdenBase(BaseModel):
    id_cliente: int
    id_estado: int
    direccion_entrega: str
    total: float
    estado: Optional[str]
    fecha: Optional[datetime]

class OrdenCreate(OrdenBase):
    pass

class Orden(OrdenBase):
    id_orden: int

    class Config:
        orm_mode = True

class OrdenDetalleBase(BaseModel):
    id_orden: int
    id_alimento: int
    id_estado: int
    cantidad: int
    precio_unitario: float
    precio_total: float

class OrdenDetalleCreate(OrdenDetalleBase):
    pass

class OrdenDetalle(OrdenDetalleBase):
    id_orden_detalle: int

    class Config:
        orm_mode = True
