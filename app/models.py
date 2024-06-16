from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(255), nullable=False)
    nombre_usuario = Column(String(100), nullable=False)
    telefono = Column(String(20))
    email = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(100), nullable=False)
    estado = Column(String(20), default="activo")

class TipoAlimento(Base):
    __tablename__ = "tipos_alimentos"

    id_tipo = Column(Integer, primary_key=True, index=True)
    nombre_tipo = Column(String(50), nullable=False)

class Alimento(Base):
    __tablename__ = "alimentos"

    id_alimento = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(100), nullable=False)
    id_tipo = Column(Integer, ForeignKey("tipos_alimentos.id_tipo"))

class EstadoOrden(Base):
    __tablename__ = "estados_ordenes"

    id_estado = Column(Integer, primary_key=True, index=True)
    nombre_estado = Column(String(50), nullable=False)

class Orden(Base):
    __tablename__ = "ordenes"

    id_orden = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("clientes.id_cliente"))
    id_estado = Column(Integer, ForeignKey("estados_ordenes.id_estado"))
    fecha = Column(datetime, default=datetime.now())
    direccion_entrega = Column(String(255), nullable=False)
    total = Column(DECIMAL(10, 2), nullable=False)
    estado = Column(String(20), default="pendiente")

class OrdenDetalle(Base):
    __tablename__ = "ordenes_detalles"

    id_orden_detalle = Column(Integer, primary_key=True, index=True)
    id_orden = Column(Integer, ForeignKey("ordenes.id_orden"))
    id_alimento = Column(Integer, ForeignKey("alimentos.id_alimento"))
    id_estado = Column(Integer, ForeignKey("estados_ordenes.id_estado"))
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(DECIMAL(10, 2), nullable=False)
    precio_total = Column(DECIMAL(10, 2), nullable=False)
