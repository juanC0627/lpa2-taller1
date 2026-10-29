from src.models.concretos.cajonera import Cajonera


class TestCajonera:
    def test_instanciacion_y_valores_por_defecto(self):
        """Verifica la asignación de atributos y valores por defecto."""
        cajonera = Cajonera("Cajonera Estándar", "Madera", "Blanco", 150)

        assert cajonera.nombre == "Cajonera Estándar"
        assert cajonera.material == "Madera"
        assert cajonera.color == "Blanco"
        assert cajonera.precio_base == 150
        assert cajonera.num_cajones == 3
        assert cajonera.tiene_ruedas is False

    def test_precio_base_none(self):
        """Verifica que si precio_base es None se asigne 0."""
        cajonera = Cajonera("Cajonera Económica", "MDF", "Gris", None)
        assert cajonera.precio_base == 0

    def test_calcular_precio_con_ruedas(self):
        """Verifica el cálculo de precio con cajones y ruedas activadas (+30)."""
        cajonera = Cajonera(
            nombre="Cajonera Móvil",
            material="Metal",
            color="Negro",
            precio_base=200,
            num_cajones=4,  # +80 (4 * 20)
            tiene_ruedas=True,  # +30
        )
        # 200 (base) + 80 (cajones) + 30 (ruedas) = 310
        assert cajonera.calcular_precio() == 310

    def test_calcular_precio_sin_ruedas(self):
        """Verifica el cálculo de precio sin ruedas."""
        cajonera = Cajonera(
            nombre="Cajonera Fija",
            material="Pino",
            color="Natural",
            precio_base=100,
            num_cajones=2,  # +40 (2 * 20)
            tiene_ruedas=False,
        )
        # 100 (base) + 40 (cajones) = 140
        assert cajonera.calcular_precio() == 140

    def test_obtener_descripcion(self):
        """Verifica la generación del texto de descripción."""
        cajonera = Cajonera(
            nombre="Cajonera Oficina",
            material="Roble",
            color="Marrón",
            precio_base=180,
            num_cajones=5,
            tiene_ruedas=True,
        )
        desc = cajonera.obtener_descripcion()

        assert "Cajonera 'Cajonera Oficina'" in desc
        assert "Material=Roble" in desc
        assert "Cajones=5" in desc
        assert "Ruedas=Sí" in desc
        assert "Precio base=$180" in desc
