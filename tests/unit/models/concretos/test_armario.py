from src.models.concretos.armario import Armario


class TestArmario:
    def test_instanciacion_y_valores_por_defecto(self):
        """Verifica la asignación correcta de atributos y valores predeterminados."""
        armario = Armario("Armario Estándar", "Madera", "Blanco", 400)

        assert armario.nombre == "Armario Estándar"
        assert armario.material == "Madera"
        assert armario.color == "Blanco"
        assert armario.precio_base == 400
        assert armario.num_puertas == 2
        assert armario.num_cajones == 0
        assert armario.tiene_espejos is False

    def test_precio_base_none(self):
        """Verifica la conversión a 0 si precio_base se pasa como None."""
        armario = Armario("Armario Económico", "MDF", "Café", None)
        assert armario.precio_base == 0

    def test_calcular_precio_con_adicionales(self):
        """Verifica el cálculo del precio con puertas, cajones y espejos."""
        armario = Armario(
            nombre="Armario Ejecutivo",
            material="Roble",
            color="Negro",
            precio_base=500,
            num_puertas=4,  # +200 (4 * 50)
            num_cajones=3,  # +90  (3 * 30)
            tiene_espejos=True,  # +100
        )
        # 500 (base) + 200 (puertas) + 90 (cajones) + 100 (espejos) = 890
        assert armario.calcular_precio() == 890

    def test_calcular_precio_sin_adicionales(self):
        """Verifica el cálculo del precio con puertas predeterminadas y sin cajones ni espejos."""
        armario = Armario(
            nombre="Armario Sencillo",
            material="Pino",
            color="Natural",
            precio_base=300,
            num_puertas=2,  # +100 (2 * 50)
            num_cajones=0,
            tiene_espejos=False,
        )
        # 300 (base) + 100 (puertas) = 400
        assert armario.calcular_precio() == 400

    def test_obtener_descripcion(self):
        """Verifica la generación de la cadena de descripción."""
        armario = Armario(
            nombre="Armario Deluxe",
            material="Cedro",
            color="Marrón",
            precio_base=600,
            num_puertas=3,
            num_cajones=2,
            tiene_espejos=True,
        )
        desc = armario.obtener_descripcion()

        assert "Armario 'Armario Deluxe'" in desc
        assert "Material=Cedro" in desc
        assert "Puertas=3" in desc
        assert "Cajones=2" in desc
        assert "Espejos=Sí" in desc
        assert "Precio base=$600" in desc
