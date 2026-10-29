import pytest

from src.models.concretos.cama import Cama


class TestCama:
    def test_herencia(self):
        """Verifica herencia de Mueble."""
        assert any(base.__name__ == "Mueble" for base in Cama.__mro__)

    def test_instanciacion_y_propiedades(self):
        """Verifica la asignación de atributos y getters."""
        cama = Cama(
            nombre="Cama King Size",
            material="Madera",
            color="Marrón",
            precio_base=500.0,
            tamaño="king",
            incluye_colchon=True,
            tiene_cabecera=True,
        )

        assert cama.nombre == "Cama King Size"
        assert cama.tamaño == "king"
        assert cama.incluye_colchon is True
        assert cama.tiene_cabecera is True

    def test_setter_tamaño_valido_e_invalido(self):
        """Verifica la validación del setter de tamaño."""
        cama = Cama("Cama Juvenil", "Pino", "Blanco", 300.0)

        # Modificación válida
        cama.tamaño = "queen"
        assert cama.tamaño == "queen"

        # Modificación inválida
        with pytest.raises(ValueError, match="Tamaño debe ser uno de:"):
            cama.tamaño = "extra-large"

    def test_calcular_precio_variaciones(self):
        """Verifica los precios calculados según los diferentes tamaños y extras."""
        # Individual + sin extras = 200
        cama_ind = Cama("Ind", "Pino", "Blanco", 200.0, tamaño="individual")
        assert cama_ind.calcular_precio() == 200.0

        # Matrimonial (+200) + Colchón (+300) = 700
        cama_mat = Cama("Mat", "Pino", "Blanco", 200.0, tamaño="matrimonial", incluye_colchon=True)
        assert cama_mat.calcular_precio() == 700.0

        # Queen (+400) + Cabecera (+100) = 700
        cama_queen = Cama("Queen", "Pino", "Blanco", 200.0, tamaño="queen", tiene_cabecera=True)
        assert cama_queen.calcular_precio() == 700.0

        # King (+600) + Colchón (+300) + Cabecera (+100) = 1200
        cama_king = Cama(
            "King",
            "Pino",
            "Blanco",
            200.0,
            tamaño="king",
            incluye_colchon=True,
            tiene_cabecera=True,
        )
        assert cama_king.calcular_precio() == 1200.0

    def test_obtener_descripcion(self):
        """Verifica la generación del texto de descripción."""
        cama = Cama("Cama Luxe", "Roble", "Negro", 400.0, tamaño="queen", incluye_colchon=True)
        desc = cama.obtener_descripcion()

        assert "Cama: Cama Luxe" in desc
        assert "Tamaño: queen" in desc
        assert "Incluye colchón: Sí" in desc
        assert "Cabecera: No" in desc
