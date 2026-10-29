import pytest

from src.models.concretos.mesa import Mesa


class TestMesa:
    def test_instanciacion_y_getters(self):
        """Verifica la asignación de atributos y getters."""
        mesa = Mesa(
            nombre="Mesa Comedor",
            material="Madera",
            color="Roble",
            precio_base=300.0,
            forma="redonda",
            largo=150.0,
            ancho=150.0,
            altura=78.0,
            capacidad_personas=6,
        )

        assert mesa.nombre == "Mesa Comedor"
        assert mesa.forma == "redonda"
        assert mesa.capacidad_personas == 6

    def test_setters_validos_e_invalidos(self):
        """Verifica las validaciones de forma y capacidad_personas."""
        mesa = Mesa("Mesa Auxiliar", "Vidrio", "Transparente", 150.0)

        # Modificaciones válidas
        mesa.forma = "cuadrada"
        mesa.capacidad_personas = 8
        assert mesa.forma == "cuadrada"
        assert mesa.capacidad_personas == 8

        # Validaciones de forma inválida
        with pytest.raises(ValueError, match="Forma debe ser una de:"):
            mesa.forma = "triangular"

        # Validaciones de capacidad inválida
        with pytest.raises(ValueError, match="La capacidad debe ser mayor a 0"):
            mesa.capacidad_personas = 0

    def test_calcular_precio_variaciones(self):
        """Verifica los cálculos de precio según forma y capacidad."""
        # Rectangular, capacidad <= 4
        m1 = Mesa("M1", "Madera", "Blanco", 200.0, forma="rectangular", capacidad_personas=4)

        # Redonda (+50), capacidad = 5 (+50)
        m2 = Mesa("M2", "Madera", "Blanco", 200.0, forma="redonda", capacidad_personas=5)

        # Ovalada (+50), capacidad = 8 (+100)
        m3 = Mesa("M3", "Madera", "Blanco", 200.0, forma="ovalada", capacidad_personas=8)

        assert m1.calcular_precio() < m2.calcular_precio()
        assert m2.calcular_precio() < m3.calcular_precio()

    def test_obtener_descripcion(self):
        """Verifica el texto descriptivo generado."""
        mesa = Mesa("Mesa Centro", "Madera", "Café", 100.0)
        desc = mesa.obtener_descripcion()

        assert "Mesa: Mesa Centro" in desc
        assert "Forma: rectangular" in desc
        assert "Capacidad: 4 personas" in desc
