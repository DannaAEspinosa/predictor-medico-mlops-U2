from flask import Flask, request, jsonify, render_template, send_file, url_for
from predictor import predecir_estado
from datetime import datetime
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

# Variables globales para llevar registro
predicciones_log = []
conteo_categorias = {}

# Función auxiliar para generar el reporte de texto
def generar_reporte_txt(ultima_fecha, conteo, ultimas_cinco):
    reporte = "Reporte de Predicciones Médicas\n"
    reporte += f"Fecha de la última predicción: {ultima_fecha}\n\n"
    reporte += "Número total de predicciones por categoría:\n"
    for cat, cnt in conteo.items():
        reporte += f"{cat}: {cnt}\n"
    reporte += "\nÚltimas 5 predicciones realizadas:\n"
    for pred in ultimas_cinco:
        reporte += f"{pred['fecha']} - {pred['resultado']}\n"
    return reporte


@app.route('/')
def home():
    return render_template("index.html", resultado=None, estudios=None)

@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener valores
    try:
        valores = (
            request.get_json().get("valores")
            if request.is_json else
            [float(request.form[k]) for k in ("valor1", "valor2", "valor3")]
        )
    except:
        return render_template("index.html", resultado="Entradas inválidas.", estudios=None)

    # Validar
    if len(valores) != 3 or all(v == 0 for v in valores):
        return render_template("index.html", resultado="Por favor, ingresa valores válidos.", estudios=None)

    # Predicción
    resultado = predecir_estado(valores)
    ts = datetime.now().isoformat()
    predicciones_log.append({"resultado": resultado, "fecha": ts})
    conteo_categorias[resultado] = conteo_categorias.get(resultado, 0) + 1

    # Estadísticas
    ultimas_cinco = predicciones_log[-5:]
    estudios = {
        "conteo": conteo_categorias,
        "ultimas_cinco": ultimas_cinco,
        "ultima_fecha": ts,
        "reporte": generar_reporte_txt(ts, conteo_categorias, ultimas_cinco)
    }

    # Guardar TXT
    txt_path = os.path.join("static", "reporte_medico.txt")
    with open(txt_path, "w") as f:
        f.write(estudios["reporte"])

    if request.is_json:
        return jsonify({"estado": resultado})
    return render_template("index.html", resultado=resultado, estudios=estudios)

@app.route('/reportes')
def reportes():
    if not predicciones_log:
        return render_template("index.html", resultado=None, estudios=None)

    ultima_fecha = predicciones_log[-1]["fecha"]
    ultimas_cinco = predicciones_log[-5:]
    estudios = {
        "conteo": conteo_categorias,
        "ultimas_cinco": ultimas_cinco,
        "ultima_fecha": ultima_fecha,
        "reporte": generar_reporte_txt(ultima_fecha, conteo_categorias, ultimas_cinco)
    }

    # Guardar TXT
    with open(os.path.join("static", "reporte_medico.txt"), "w") as f:
        f.write(estudios["reporte"])

    return render_template("index.html", resultado=None, estudios=estudios)



@app.route('/descargar_txt')
def descargar_txt():
    txt_path = os.path.join("static", "reporte_medico.txt")
    return send_file(txt_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
