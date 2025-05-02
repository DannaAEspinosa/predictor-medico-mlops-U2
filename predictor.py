def predecir_estado(valores):
    if not isinstance(valores, list) or len(valores) != 3 or not all(isinstance(v, (int, float)) for v in valores):
        return "ENTRADA INVÁLIDA"

    suma = sum(valores)
    if suma <= 100:
        return "NO ENFERMO"
    elif suma <= 200:
        return "ENFERMEDAD LEVE"
    elif suma <= 300:
        return "ENFERMEDAD AGUDA"
    else:
        return "ENFERMEDAD CRÓNICA"
