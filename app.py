from flask import Flask, request, jsonify, render_template
from predictor import predecir_estado

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", resultado=None)

@app.route('/predecir', methods=['POST'])
def predecir():
    # Si la solicitud es JSON, obtenemos los valores como un JSON
    if request.is_json:
        valores = request.get_json().get("valores", [])
    else:
        try:
            # Si la solicitud no es JSON, obtenemos los valores del formulario
            v1 = float(request.form.get("valor1", 0))
            v2 = float(request.form.get("valor2", 0))
            v3 = float(request.form.get("valor3", 0))
            valores = [v1, v2, v3]
        except ValueError:
            return render_template("index.html", resultado="Entradas inválidas. Asegúrate de ingresar números válidos.")

    # Llamamos a la función de predicción
    resultado = predecir_estado(valores)
    

    # Si la solicitud es JSON, respondemos con JSON
    if request.is_json:
        return jsonify({"estado": resultado})
    else:
        # Si no es JSON, redirigimos al formulario con el resultado de la predicción
        return render_template("index.html", resultado=resultado)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
