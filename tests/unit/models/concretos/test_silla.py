import pytest

from src.models.categorias.asientos import Asiento
from src.models.concretos.silla import Silla
from src.models.mueble import Mueble


class TestSilla:
    def test_herencia(self):
        """Verifica herencia de Asiento y Mueble."""
        assert issubclass(Silla, Asiento)
        assert issubclass(Silla, Mueble)

    def test_instanciacion_y_propiedades(self):
        """Verifica la asignación de atributos y getters/setters."""
        silla = Silla(
            nombre="Silla Ejecutiva",
            material="Cuero Synt",
            color="Negro",
            precio_base=150.0,
            tiene_respaldo=True,
            material_tapizado="Cuero",
            altura_regulable=True,
            tiene_ruedas=True,
        )

        assert silla.nombre == "Silla Ejecutiva"
        assert silla.precio_base == 150.0
        assert silla.capacidad_personas == 1
        assert silla.tiene_respaldo is True
        assert silla.material_tapizado == "Cuero"
        assert silla.altura_regulable is True
        assert silla.tiene_ruedas is True

        # Probar setters
        silla.altura_regulable = False
        silla.tiene_ruedas = False
        assert silla.altura_regulable is False
        assert silla.tiene_ruedas is False

    def test_calcular_precio_con_adicionales(self):
        """Verifica cálculo de precio con altura regulable (+30) y ruedas (+20)."""
        silla = Silla(
            nombre="Silla Gamer",
            material="Plástico/Metal",
            color="Rojo",
            precio_base=100.0,
            tiene_respaldo=True,
            material_tapizado="Tela",
            altura_regulable=True,
            tiene_ruedas=True,
        )
        # Factor comodidad con respaldo + Tela = 1.0 + 0.1 (respaldo) + 0.1 (tela) = 1.2
        # Precio = 100.0 * 1.2 + 30 (altura) + 20 (ruedas) = 170.0
        assert silla.calcular_precio() == pytest.approx(170.0)

    def test_obtener_descripcion(self):
        """Verifica generación del texto de descripción."""
        silla = Silla("Silla Comedor", "Madera", "Blanco", 80.0, True)
        desc = silla.obtener_descripcion()
        assert "Silla: Silla Comedor" in desc
        assert "Altura regulable: No" in desc
        assert "Ruedas: No" in desc

    def test_regular_altura(self):
        """Verifica el método regular_altura para sillas fijas y regulables."""
        silla_fija = Silla("Silla Fija", "Madera", "Marrón", 50.0, altura_regulable=False)
        assert silla_fija.regular_altura(50) == "Esta silla no tiene altura regulable"

        silla_regulable = Silla("Silla Oficina", "Metal", "Negro", 100.0, altura_regulable=True)
        assert silla_regulable.regular_altura(30) == "La altura debe estar entre 40 y 100 cm"
        assert silla_regulable.regular_altura(110) == "La altura debe estar entre 40 y 100 cm"
        assert silla_regulable.regular_altura(50) == "Altura ajustada a 50 cm"

    def test_es_silla_oficina(self):
        """Verifica si es silla de oficina (requiere ruedas y altura regulable)."""
        silla_oficina = Silla("Oficina", "Metal", "Negro", 100.0, altura_regulable=True, tiene_ruedas=True)
        silla_comun = Silla("Común", "Madera", "Blanco", 50.0, altura_regulable=True, tiene_ruedas=False)

        assert silla_oficina.es_silla_oficina() is True
        assert silla_comun.es_silla_oficina() is False
