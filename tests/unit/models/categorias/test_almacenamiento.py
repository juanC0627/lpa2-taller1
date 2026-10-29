import pytest

from src.models.categorias.almacenamiento import Almacenamiento
from src.models.mueble import Mueble


# Subclase concreta auxiliar para instanciar la clase abstracta Almacenamiento
class AlmacenamientoConcreto(Almacenamiento):
    def calcular_precio(self) -> float:
        return self.precio_base * self.calcular_factor_almacenamiento()

    def obtener_descripcion(self) -> str:
        return f"{self.nombre} - {self.obtener_info_almacenamiento()}"


class TestAlmacenamiento:
    def test_herencia_de_mueble(self):
        """Verifica que Almacenamiento sea subclase de Mueble."""
        assert issubclass(Almacenamiento, Mueble)

    def test_atributos_y_getters(self):
        """Verifica la asignación correcta de num_compartimentos y capacidad_litros."""
        mueble = AlmacenamientoConcreto("Armario", "Madera", "Café", 300.0, 4, 500.0)
        assert mueble.num_compartimentos == 4
        assert mueble.capacidad_litros == 500.0

    def test_setters_validos_e_invalidos(self):
        """Verifica asignación y excepciones en las propiedades."""
        mueble = AlmacenamientoConcreto("Cajonera", "Madera", "Blanco", 150.0, 3, 200.0)

        # Asignaciones válidas
        mueble.num_compartimentos = 5
        mueble.capacidad_litros = 300.0
        assert mueble.num_compartimentos == 5
        assert mueble.capacidad_litros == 300.0

        # Validaciones de valores no válidos (<= 0)
        with pytest.raises(ValueError, match="La capacidad debe ser mayor a 0"):
            mueble.capacidad_litros = 0

        with pytest.raises(ValueError, match="El número de compartimentos debe ser mayor a 0"):
            mueble.num_compartimentos = 0

    def test_calcular_factor_almacenamiento(self):
        """Factor: 1.0 + (num_compartimentos - 1)*0.05 + (capacidad_litros/100)*0.02."""
        # Factor = 1.0 + (4 - 1)*0.05 + (500/100)*0.02 = 1.0 + 0.15 + 0.10 = 1.25
        mueble = AlmacenamientoConcreto("Armario", "Madera", "Café", 300.0, 4, 500.0)
        assert mueble.calcular_factor_almacenamiento() == pytest.approx(1.25)

    def test_obtener_info_almacenamiento(self):
        """Verifica el formato del texto devuelto por obtener_info_almacenamiento."""
        mueble = AlmacenamientoConcreto("Armario", "Madera", "Café", 300.0, 2, 150.0)
        assert mueble.obtener_info_almacenamiento() == "Compartimentos: 2, Capacidad: 150.0L"
