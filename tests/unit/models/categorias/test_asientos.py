from abc import ABC

import pytest

from src.models.categorias.asientos import Asiento
from src.models.mueble import Mueble


# Subclase concreta auxiliar para instanciar la clase abstracta Asiento
class AsientoConcreto(Asiento):
    def calcular_precio(self) -> float:
        return self.precio_base * self.calcular_factor_comodidad()

    def obtener_descripcion(self) -> str:
        return f"{self.nombre} - {self.obtener_info_asiento()}"


class TestAsientos:
    # --- PRUEBAS DE ABSTRACCIÓN Y HERENCIA ---
    def test_es_clase_abstracta_y_hereda_de_mueble(self):
        """Verifica herencia de Mueble y que sea abstracta."""

        assert issubclass(Asiento, Mueble)
        assert issubclass(Asiento, ABC)

        # Verificar que no se pueda instanciar directamente la clase Asiento
        with pytest.raises(TypeError):
            Asiento("Silla", "Madera", "Negro", 100.0, 1, True)

    # --- PRUEBAS DE GETTERS Y SETTERS ---
    def test_getters_y_setters_basicos(self):
        """Verifica asignación y modificación de propiedades."""
        asiento = AsientoConcreto("Silla", "Madera", "Negro", 100.0, 1, True, "Tela")

        assert asiento.capacidad_personas == 1
        assert asiento.tiene_respaldo is True
        assert asiento.material_tapizado == "Tela"

        asiento.capacidad_personas = 3
        asiento.tiene_respaldo = False
        asiento.material_tapizado = "Cuero"

        assert asiento.capacidad_personas == 3
        assert asiento.tiene_respaldo is False
        assert asiento.material_tapizado == "Cuero"

    def test_setter_capacidad_invalida(self):
        """Verifica validación cuando la capacidad es menor o igual a 0."""
        asiento = AsientoConcreto("Silla", "Madera", "Negro", 100.0, 1, True)

        with pytest.raises(ValueError, match="La capacidad debe ser mayor a 0"):
            asiento.capacidad_personas = 0

        with pytest.raises(ValueError, match="La capacidad debe ser mayor a 0"):
            asiento.capacidad_personas = -1

    # --- PRUEBAS DE MÉTODOS CONCRETOS ---
    def test_calcular_factor_comodidad_cuero(self):
        """Factor: 1.0 + 0.1 (respaldo) + 0.2 (cuero) + (2-1)*0.05 = 1.35"""
        asiento = AsientoConcreto("Sillón", "Madera", "Marrón", 200.0, 2, True, "Cuero")
        assert asiento.calcular_factor_comodidad() == pytest.approx(1.35)

    def test_calcular_factor_comodidad_tela_sin_respaldo(self):
        """Factor: 1.0 + 0.0 (sin respaldo) + 0.1 (tela) + 0.0 = 1.1"""
        asiento = AsientoConcreto("Banco", "Metal", "Gris", 80.0, 1, False, "Tela")
        assert asiento.calcular_factor_comodidad() == pytest.approx(1.1)

    def test_obtener_info_asiento(self):
        """Verifica cadenas generadas por obtener_info_asiento."""
        asiento_con_tapiz = AsientoConcreto("Silla", "Madera", "Negro", 100.0, 1, True, "Cuero")
        asiento_sin_tapiz = AsientoConcreto("Taburete", "Metal", "Gris", 50.0, 1, False)

        assert "Capacidad: 1 personas, Respaldo: Sí, Tapizado: Cuero" in asiento_con_tapiz.obtener_info_asiento()
        assert "Capacidad: 1 personas, Respaldo: No" in asiento_sin_tapiz.obtener_info_asiento()
        assert "Tapizado" not in asiento_sin_tapiz.obtener_info_asiento()
