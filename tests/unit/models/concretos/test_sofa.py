from src.models.concretos.sofa import Sofa


class TestSofa:
    def test_instanciacion_y_propiedades(self):
        """Verifica atributos y creación de un Sofá."""
        sofa = Sofa("Sofá Modular", "Tela", "Gris", 800, capacidad_personas=3)
        assert sofa.nombre == "Sofá Modular"
        assert sofa.material == "Tela"
        assert sofa.color == "Gris"
        assert sofa.precio_base == 800
        assert sofa.capacidad_personas == 3

    def test_calcular_precio(self):
        """Verifica el cálculo de precio de Sofá."""
        sofa = Sofa("Sofá Deluxe", "Piel", "Negro", 1000, capacidad_personas=4)
        assert sofa.calcular_precio() >= 1000

    def test_obtener_descripcion(self):
        """Verifica la generación de la descripción."""
        sofa = Sofa("Sofá Cama Lux", "Cuero", "Café", 1200)
        desc = sofa.obtener_descripcion()
        assert "Sofá" in desc or "Sofá Cama Lux" in desc
