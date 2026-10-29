from src.models.concretos.cama import Cama
from src.models.concretos.sofa import Sofa
from src.models.concretos.sofacama import SofaCama


class TestSofaCama:
    def test_herencia_multiple(self):
        """Verifica la herencia múltiple desde Sofa y Cama."""
        assert issubclass(SofaCama, Sofa)
        assert issubclass(SofaCama, Cama)

    def test_instanciacion_y_getters(self):
        """Verifica la asignación de atributos, propiedades y getters."""
        sofacama = SofaCama(
            nombre="SofáCama Moderno",
            material="Madera/Metal",
            color="Gris",
            precio_base=800,
            capacidad_personas=3,
            material_tapizado="Tela",
            tamaño_cama="queen",
            incluye_colchon=True,
            mecanismo_conversion="hidraulico",
        )

        assert sofacama.nombre == "SofáCama Moderno"
        assert sofacama.mecanismo_conversion == "hidraulico"
        assert sofacama.modo_actual == "sofa"
        assert sofacama.tamaño == "queen"
        assert sofacama.tamaño_cama == "queen"

    def test_calcular_precio_variaciones(self):
        """Prueba las variaciones de precio por tamaño y mecanismos de conversión."""
        # Matrimonial + Hidráulico + Colchón
        sc1 = SofaCama(
            "SC 1",
            "Pino",
            "Azul",
            500,
            tamaño_cama="matrimonial",
            mecanismo_conversion="hidraulico",
            incluye_colchon=True,
        )
        # Queen + Eléctrico + Colchón
        sc2 = SofaCama(
            "SC 2",
            "Pino",
            "Rojo",
            500,
            tamaño_cama="queen",
            mecanismo_conversion="electrico",
            incluye_colchon=True,
        )
        # King + Mecanismo estándar + Sin colchón
        sc3 = SofaCama(
            "SC 3",
            "Pino",
            "Negro",
            500,
            tamaño_cama="king",
            mecanismo_conversion="plegable",
            incluye_colchon=False,
        )
        # Individual + Mecanismo estándar
        sc4 = SofaCama(
            "SC 4",
            "Pino",
            "Verde",
            500,
            tamaño_cama="individual",
            mecanismo_conversion="plegable",
            incluye_colchon=False,
        )

        assert sc1.calcular_precio() > 500
        assert sc2.calcular_precio() > sc1.calcular_precio()
        assert sc3.calcular_precio() > 500
        assert sc4.calcular_precio() >= 500

    def test_convertir_a_cama_y_a_sofa(self):
        """Verifica la lógica de conversión entre modos."""
        sc = SofaCama("SC Convertible", "Metal", "Negro", 600, mecanismo_conversion="plegable")

        # Estado inicial es sofa
        assert sc.convertir_a_sofa() == "El sofá-cama ya está en modo sofá"

        # Convertir a cama
        res_cama = sc.convertir_a_cama()
        assert "Sofá convertido a cama" in res_cama
        assert sc.modo_actual == "cama"
        assert sc.convertir_a_cama() == "El sofá-cama ya está en modo cama"

        # Convertir de nuevo a sofa
        res_sofa = sc.convertir_a_sofa()
        assert "Cama convertida a sofá" in res_sofa
        assert sc.modo_actual == "sofa"

    def test_obtener_descripcion(self):
        """Verifica el texto descriptivo del Sofá-Cama."""
        sc = SofaCama("SofaCama Comfort", "Tela", "Beige", 700)
        desc = sc.obtener_descripcion()

        assert "Sofá-Cama: SofaCama Comfort" in desc
        assert "Tamaño como cama: matrimonial" in desc
        assert "Mecanismo: plegable" in desc
        assert "Modo actual: sofa" in desc

    def test_obtener_capacidad_total(self):
        """Verifica el diccionario de capacidad según tamaño."""
        sc_matrimonial = SofaCama(
            "SC Matrimonial",
            "Tela",
            "Gris",
            500,
            capacidad_personas=3,
            tamaño_cama="matrimonial",
        )
        caps1 = sc_matrimonial.obtener_capacidad_total()
        assert caps1["como_sofa"] == 3
        assert caps1["como_cama"] == 2

        sc_individual = SofaCama(
            "SC Individual",
            "Tela",
            "Gris",
            500,
            capacidad_personas=2,
            tamaño_cama="individual",
        )
        caps2 = sc_individual.obtener_capacidad_total()
        assert caps2["como_sofa"] == 2
        assert caps2["como_cama"] == 1

    def test_str_representation(self):
        """Verifica el método __str__."""
        sc = SofaCama("Multifuncional", "Metal", "Blanco", 400)
        assert str(sc) == "Sofá-cama Multifuncional (modo: sofa)"
