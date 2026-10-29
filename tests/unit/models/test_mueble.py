import pytest

from src.models.mueble import Mueble


# 1. Crear una subclase concreta dummy solo para poder instanciar Mueble en las pruebas
class MuebleConcreto(Mueble):
    def calcular_precio(self) -> float:
        return self.precio_base

    def obtener_descripcion(self) -> str:
        return f"{self.nombre} de prueba"


class TestMueble:
    # --- PRUEBAS DE ABSTRACCIÓN ---
    def test_es_clase_abstracta(self):
        """Verifica que Mueble no se puede instanciar directamente."""
        with pytest.raises(TypeError):
            Mueble("Mesa", "Madera", "Marrón", 100.0)

    def test_tiene_metodos_abstractos(self):
        """Verifica que existen los métodos abstractos obligatorios."""
        assert hasattr(Mueble, "calcular_precio")
        assert hasattr(Mueble, "obtener_descripcion")
        assert Mueble.calcular_precio.__isabstractmethod__
        assert Mueble.obtener_descripcion.__isabstractmethod__

    # --- PRUEBAS DE INSTANCIACIÓN Y GETTERS ---
    def test_inicializacion_y_getters(self):
        """Verifica que el constructor asigne correctamente los valores."""
        obj = MuebleConcreto("Silla", "Madera", "Negro", 150.0)
        assert obj.nombre == "Silla"
        assert obj.material == "Madera"
        assert obj.color == "Negro"
        assert obj.precio_base == 150.0

    # --- PRUEBAS DE SETTERS Y VALIDACIONES ---
    def test_setters_validos(self):
        """Verifica la modificación correcta de los atributos mediante setters."""
        obj = MuebleConcreto("Silla", "Madera", "Negro", 150.0)
        obj.nombre = "  Silla Ejecutiva  "
        obj.material = " Cuero "
        obj.color = " Blanco "
        obj.precio_base = 200.0

        assert obj.nombre == "Silla Ejecutiva"
        assert obj.material == "Cuero"
        assert obj.color == "Blanco"
        assert obj.precio_base == 200.0

    def test_validaciones_setters_invalidos(self):
        """Verifica que los setters lancen ValueError con datos inválidos."""
        obj = MuebleConcreto("Silla", "Madera", "Negro", 150.0)

        with pytest.raises(ValueError, match="El nombre no puede estar vacío"):
            obj.nombre = "   "

        with pytest.raises(ValueError, match="El material no puede estar vacío"):
            obj.material = ""

        with pytest.raises(ValueError, match="El color no puede estar vacío"):
            obj.color = None

        with pytest.raises(ValueError, match="El precio base no puede ser negativo"):
            obj.precio_base = -10.0

    # --- PRUEBAS DE MÉTODOS MÁGICOS (__str__ y __repr__) ---
    def test_representacion_str_y_repr(self):
        """Verifica las representaciones en texto de la clase."""
        obj = MuebleConcreto("Escritorio", "Metal", "Gris", 300.0)

        assert str(obj) == "Escritorio de Metal en color Gris"
        assert repr(obj) == "Mueble(nombre='Escritorio', material='Metal', color='Gris', precio_base=300.0)"
