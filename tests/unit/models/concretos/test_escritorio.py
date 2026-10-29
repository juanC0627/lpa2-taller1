from src.models.concretos.escritorio import Escritorio


class TestEscritorio:
    def test_instanciacion_y_valores_por_defecto(self):
        """Verifica la asignación de atributos y valores predeterminados."""
        escritorio = Escritorio("Escritorio Básico", "Madera", "Blanco", 200)

        assert escritorio.nombre == "Escritorio Básico"
        assert escritorio.material == "Madera"
        assert escritorio.color == "Blanco"
        assert escritorio.precio_base == 200
        assert escritorio.forma == "rectangular"
        assert escritorio.tiene_cajones is False
        assert escritorio.num_cajones == 0
        assert escritorio.largo == 1.2
        assert escritorio.tiene_iluminacion is False

    def test_precio_base_none(self):
        """Verifica la conversión a 0 si precio_base se pasa como None."""
        escritorio = Escritorio("Escritorio Económico", "MDF", "Negro", None)
        assert escritorio.precio_base == 0

    def test_calcular_precio_con_adicionales(self):
        """Verifica el cálculo de precio con cajones, largo > 1.5m, iluminación y forma en L."""
        escritorio = Escritorio(
            nombre="Escritorio Gamer",
            material="Metal",
            color="Negro",
            precio_base=300,
            forma="L",  # +30
            tiene_cajones=True,
            num_cajones=3,  # +75 (3 * 25)
            largo=1.8,  # +50 (> 1.5)
            tiene_iluminacion=True,  # +40
        )
        # 300 (base) + 75 (cajones) + 50 (largo) + 40 (iluminación) + 30 (forma) = 495
        assert escritorio.calcular_precio() == 495

    def test_calcular_precio_sin_adicionales(self):
        """Verifica precio base directo cuando no cumple condiciones adicionales."""
        escritorio = Escritorio(
            nombre="Escritorio Simple",
            material="Madera",
            color="Café",
            precio_base=150,
            largo=1.2,
            tiene_cajones=False,
            tiene_iluminacion=False,
            forma="rectangular",
        )
        assert escritorio.calcular_precio() == 150

    def test_obtener_descripcion(self):
        """Verifica la generación del formato de descripción."""
        escritorio = Escritorio(
            nombre="Pro",
            material="Roble",
            color="Natural",
            precio_base=250,
            tiene_cajones=True,
            num_cajones=2,
            tiene_iluminacion=True,
        )
        desc = escritorio.obtener_descripcion()

        assert "Escritorio 'Pro'" in desc
        assert "Forma=rectangular" in desc
        assert "Cajones=2" in desc
        assert "Iluminación=Sí" in desc
        assert "Precio base=$250" in desc
