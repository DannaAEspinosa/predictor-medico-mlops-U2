import pytest
from predictor import predecir_estado

@pytest.mark.parametrize("valores, esperado", [
    ([10, 20, 30], "NO ENFERMO"),          # suma = 60
    ([50, 60, 90], "ENFERMEDAD LEVE"),     # suma = 200
    ([100, 100, 50], "ENFERMEDAD AGUDA"),  # suma = 250
    ([100, 150, 150], "ENFERMEDAD CRÓNICA"),  # suma = 400
    ([200, 200, 200], "ENFERMEDAD TERMINAL"),  # suma = 600
    ([99.9, 100, 1], "ENFERMEDAD AGUDA"),       # suma ≈ 200
    ([199.9, 199.9, 0], "ENFERMEDAD CRÓNICA"),  # suma ≈ 400
    ([150, 150, 150], "ENFERMEDAD TERMINAL")  # suma = 450
])
def test_predecir_estado_categorias(valores, esperado):
    assert predecir_estado(valores) == esperado

def test_predecir_estado_entrada_invalida():
    assert predecir_estado("foo") == "ENTRADA INVÁLIDA"
    assert predecir_estado([1, 2]) == "ENTRADA INVÁLIDA"  # menos de 3 valores
    assert predecir_estado([0, 0, 0]) == "NO ENFERMO"   # suma = 0
    assert predecir_estado([100, 100, "abc"]) == "ENTRADA INVÁLIDA"  # tipo inválido
    assert predecir_estado([-10, 50, 60]) == "NO ENFERMO"  # valor negativo


def test_prediccion_limite():
    # Pruebas en los límites exactos
    assert predecir_estado([100, 50, 50]) == "ENFERMEDAD LEVE"  # suma = 200
    assert predecir_estado([199.99, 0.01, 0]) == "ENFERMEDAD LEVE"  # suma ≈ 200
