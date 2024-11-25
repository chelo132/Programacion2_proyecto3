# Definición de modelos clases etc.
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    
    email = Column(String, primary_key=True)  # Email como clave primaria
    nombre = Column(String, nullable=False)
    edad= Column(Integer, nullable=False)
    pedidos = relationship("Pedido", back_populates="cliente", cascade="all, delete-orphan")

class Pedido(Base):
    __tablename__ = 'pedidos'
    
    id = Column(Integer, primary_key=True, autoincrement=True )
    descripcion = Column(String, nullable=False)
    cliente_email = Column(String, ForeignKey('clientes.email', onupdate="CASCADE"), nullable=False)
    cliente = relationship("Cliente", back_populates="pedidos")

class Ingrediente(Base):
    __tablename__ = 'ingredientes'

    id_ingrediente = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), nullable=False)
    tipo = Column(String(50), nullable=False)
    cantidad = Column(Integer, nullable=False)
    unidad_de_medida = Column(String(20), nullable=False)

class Menu(Base):
    __tablename__ = 'menu'

    id_menu = Column(Integer, primary_key=True, autoincrement=True)
    nombre_menu = Column(String(50), nullable=False)
    descripcion = Column(String(255), nullable=True)