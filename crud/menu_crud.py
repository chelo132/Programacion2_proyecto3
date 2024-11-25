from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models import Menu

class MenuCRUD:
    @staticmethod
    def crear_menu(db: Session, nombre_menu: str, descripcion: str = None):
        """Crea un nuevo menú en la base de datos."""
        menu_existente = db.query(Menu).filter_by(nombre_menu=nombre_menu).first()
        if menu_existente:
            print(f"El menú '{nombre_menu}' ya existe.")
            return menu_existente

        menu = Menu(nombre_menu=nombre_menu, descripcion=descripcion)
        db.add(menu)
        try:
            db.commit()
            db.refresh(menu)
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error al crear el menú: {e}")
            return None
        return menu

    @staticmethod
    def leer_menus(db: Session):
        """Obtiene todos los menús de la base de datos."""
        try:
            return db.query(Menu).all()
        except SQLAlchemyError as e:
            print(f"Error al leer los menús: {e}")
            return []

    @staticmethod
    def actualizar_menu(db: Session, id_menu: int, nuevo_nombre_menu: str = None, nueva_descripcion: str = None):
        """Actualiza los datos de un menú existente."""
        menu = db.query(Menu).get(id_menu)
        if not menu:
            print(f"No se encontró el menú con ID '{id_menu}'.")
            return None

        if nuevo_nombre_menu:
            menu.nombre_menu = nuevo_nombre_menu
        if nueva_descripcion is not None:
            menu.descripcion = nueva_descripcion

        try:
            db.commit()
            db.refresh(menu)
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error al actualizar el menú: {e}")
            return None
        return menu

    @staticmethod
    def borrar_menu(db: Session, id_menu: int):
        """Elimina un menú de la base de datos."""
        menu = db.query(Menu).get(id_menu)
        if not menu:
            print(f"No se encontró el menú con ID '{id_menu}'.")
            return None

        db.delete(menu)
        try:
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Error al borrar el menú: {e}")
            return None
        return menu
