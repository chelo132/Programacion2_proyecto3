from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import Ingrediente

class IngredienteCRUD:
    @staticmethod
    def crear_ingrediente(db: Session, nombre: str, tipo: str, cantidad: int, unidad_de_medida: str):
        """Crea un nuevo ingrediente en la base de datos."""
        ingrediente_existente = db.query(Ingrediente).filter_by(nombre=nombre, tipo=tipo).first()
        if ingrediente_existente:
            print(f"El ingrediente '{nombre}' de tipo '{tipo}' ya existe.")
            return ingrediente_existente

        ingrediente = Ingrediente(
            nombre=nombre,
            tipo=tipo,
            cantidad=cantidad,
            unidad_de_medida=unidad_de_medida
        )
        db.add(ingrediente)
        try:
            db.commit()
            db.refresh(ingrediente)
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error al crear el ingrediente: {e}")
            return None
        return ingrediente

    @staticmethod
    def leer_ingredientes(db: Session):
        """Obtiene todos los ingredientes de la base de datos."""
        try:
            return db.query(Ingrediente).all()
        except SQLAlchemyError as e:
            print(f"Error al leer los ingredientes: {e}")
            return []

    @staticmethod
    def actualizar_ingrediente(
        db: Session, 
        id_ingrediente: int, 
        nuevo_nombre: str = None, 
        nuevo_tipo: str = None, 
        nueva_cantidad: int = None, 
        nueva_unidad_de_medida: str = None
    ):
        """Actualiza los datos de un ingrediente existente."""
        ingrediente = db.query(Ingrediente).get(id_ingrediente)
        if not ingrediente:
            print(f"No se encontró el ingrediente con ID '{id_ingrediente}'.")
            return None

        if nuevo_nombre:
            ingrediente.nombre = nuevo_nombre
        if nuevo_tipo:
            ingrediente.tipo = nuevo_tipo
        if nueva_cantidad is not None:
            ingrediente.cantidad = nueva_cantidad
        if nueva_unidad_de_medida:
            ingrediente.unidad_de_medida = nueva_unidad_de_medida

        try:
            db.commit()
            db.refresh(ingrediente)
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error al actualizar el ingrediente: {e}")
            return None
        return ingrediente

    @staticmethod
    def borrar_ingrediente(db: Session, id_ingrediente: int):
        """Elimina un ingrediente de la base de datos."""
        ingrediente = db.query(Ingrediente).get(id_ingrediente)
        if not ingrediente:
            print(f"No se encontró el ingrediente con ID '{id_ingrediente}'.")
            return None

        db.delete(ingrediente)
        try:
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error al borrar el ingrediente: {e}")
            return None
        return ingrediente
