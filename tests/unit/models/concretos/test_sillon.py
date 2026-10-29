from src.models.concretos.sillon import Sillon


class TestSillon:
    def test_instanciacion_y_valores_por_defecto(self):
        """Verifica la asignación correcta de atributos y valores por defecto."""
        sillon = Sillon("Sillón Ejecutivo", "Cuero", "Negro", 500)

        assert sillon.nombre == "Sillón Ejecutivo"
        assert sillon.material == "Cuero"
        assert sillon.color == "Negro"
        assert sillon.precio_base == 500
        assert sillon.capacidad_personas == 2
        assert sillon.tiene_respaldo is True
        assert sillon.material_tapizado is None
        assert sillon.tiene_brazos is True
        assert sillon.es_reclinable is False
        assert sillon.tiene_reposapiés is False

    def test_precio_base_none(self):
        """Verifica que si precio_base es None se asigne 0."""
        sillon = Sillon("Sillón Económico", "Tela", "Gris", None)
        assert sillon.precio_base == 0

    def test_calcular_precio_con_adicionales(self):
        """Verifica el cálculo del precio con todos los accesorios activos."""
        sillon = Sillon(
            nombre="Sillón Relax",
            material="Piel",
            color="Marrón",
            precio_base=1000,
            material_tapizado="Cuero Sintético",
            tiene_brazos=True,  # +100
            es_reclinable=True,  # +250
            tiene_reposapiés=True,  # +80
        )
        # 1000 (base) + 200 (tapizado) + 100 (brazos) + 250 (reclinable) + 80 (reposapiés) = 1630
        assert sillon.calcular_precio() == 1630

    def test_calcular_precio_sin_adicionales(self):
        """Verifica el cálculo del precio sin tapizado, ni brazos, ni reclinable, ni reposapiés."""
        sillon = Sillon(
            nombre="Sillón Básico",
            material="Madera",
            color="Blanco",
            precio_base=300,
            tiene_brazos=False,
        )
        # 300 (base)
        assert sillon.calcular_precio() == 300

    def test_obtener_descripcion(self):
        """Verifica que la cadena de descripción contenga las propiedades principales."""
        sillon = Sillon(
            nombre="Comfort Plus",
            material="Tela",
            color="Azul",
            precio_base=400,
            material_tapizado="Algodón",
            es_reclinable=True,
        )
        desc = sillon.obtener_descripcion()

        assert "Sillón 'Comfort Plus'" in desc
        assert "Material=Tela" in desc
        assert "Tapizado=Algodón" in desc
        assert "Reclinable=Sí" in desc
        assert "Reposapiés=No" in desc
        assert "Precio base=$400" in desc
