import os
import json
import tempfile
import pytest
from datetime import datetime
from app import app, predicciones_log, conteo_categorias  # ajusta import si tu módulo principal es distinto

@pytest.fixture(autouse=True)
def clear_logs():
    # Antes de cada test, limpia los registros
    predicciones_log.clear()
    conteo_categorias.clear()
    yield
    predicciones_log.clear()
    conteo_categorias.clear()

def test_reports_empty(client):
    # sin predicciones, /reportes debería mostrar estudios=None
    response = client.get("/reportes")
    assert response.status_code == 200
    assert "Reporte de estadísticas".encode('utf-8') not in response.data

def test_reports_after_predictions(client):
    # simula 6 predicciones vía POST
    for i in range(6):
        client.post("/predecir", data={
            "valor1": str(10*(i+1)),
            "valor2": "0",
            "valor3": "0"
        })
    # ahora hay 6 elementos, ultimas_cinco debe ser 5
    response = client.get("/reportes")
    assert response.status_code == 200
    html = response.data.decode()
    assert "Total de predicciones por categoría" in html
    # verifica que aparecen 5 líneas en sección de últimas 5
    assert html.count("<li") >= 5
