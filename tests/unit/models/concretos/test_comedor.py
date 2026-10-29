from src.models.concretos.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


class TestComedor:
    def test_instanciacion_y_sillas_por_defecto(self):
        """Verifica la creación del comedor con lista de sillas por defecto o vacía."""
        mesa = Mesa("Mesa Principal", "Madera", "Marrón", 200.0)
        comedor = Comedor(mesa=mesa)

        assert comedor.mesa == mesa
        assert comedor.sillas == []
        assert comedor.cantidad_sillas() == 0

    def test_agregar_y_quitar_silla(self):
        """Verifica la gestión de sillas (agregar, contar y remover)."""
        mesa = Mesa("Mesa Comedor", "Roble", "Café", 300.0)
        silla1 = Silla("Silla 1", "Madera", "Café", 50.0)
        silla2 = Silla("Silla 2", "Madera", "Café", 50.0)
        silla_no_agregada = Silla("Silla Externa", "Metal", "Negro", 40.0)

        comedor = Comedor(mesa=mesa, sillas=[silla1])
        assert comedor.cantidad_sillas() == 1

        # Agregar silla
        comedor.agregar_silla(silla2)
        assert comedor.cantidad_sillas() == 2
        assert silla2 in comedor.sillas

        # Intentar quitar silla que NO está en el comedor (cubre la rama if)
        comedor.quitar_silla(silla_no_agregada)
        assert comedor.cantidad_sillas() == 2

        # Quitar silla existente
        comedor.quitar_silla(silla1)
        assert comedor.cantidad_sillas() == 1
        assert silla1 not in comedor.sillas

    def test_calcular_precio_total(self):
        """Verifica la suma del precio de la mesa más las sillas."""
        mesa = Mesa(
            "Mesa Rectangular",
            "Madera",
            "Blanco",
            200.0,
            forma="rectangular",
            capacidad_personas=4,
        )
        silla1 = Silla("Silla 1", "Madera", "Blanco", 50.0)
        silla2 = Silla("Silla 2", "Madera", "Blanco", 50.0)

        comedor = Comedor(mesa=mesa, sillas=[silla1, silla2])

        precio_esperado = mesa.calcular_precio() + silla1.calcular_precio() + silla2.calcular_precio()
        assert comedor.calcular_precio_total() == precio_esperado

    def test_descripcion(self):
        """Verifica la generación del formato de texto para la descripción."""
        mesa = Mesa("Mesa Familiar", "Madera", "Marrón", 250.0)
        silla = Silla("Silla Confort", "Madera", "Marrón", 60.0)

        comedor = Comedor(mesa=mesa, sillas=[silla])
        desc = comedor.descripcion()

        assert "Comedor con mesa:" in desc
        assert "y 1 sillas:" in desc
        assert "1. Silla:" in desc or "1." in desc
