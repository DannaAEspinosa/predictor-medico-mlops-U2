# 🩺 Predictor Médico – Proyecto MLOps

Este repositorio contiene un pipeline básico de MLOps que simula un sistema de predicción médica. A través de una interfaz web, el usuario puede ingresar tres valores clínicos numéricos y obtener un diagnóstico estimado. La lógica de predicción está contenida en un archivo Python y la aplicación está empaquetada en un contenedor Docker listo para su despliegue.

---

## 📌 Objetivo

Simular un modelo de predicción de enfermedades comunes y huérfanas a partir de tres síntomas como parte de una práctica de desarrollo MLOps end-to-end. El proyecto tiene como fin construir un flujo de trabajo reproducible y mantenible que abarque:

- Desarrollo local  
- Empaquetado y despliegue con Docker  
- Automatización del ciclo de vida del modelo (CI/CD con GitHub Actions)  
- Control de versiones y documentación con GitHub  
- Publicación de imágenes en GitHub Container Registry (GHCR)

---

## 🚀 Instrucciones

### 1. Clonar el repositorio

```bash
git clone https://github.com/DannaAEspinosa/predictor-medico-mlops-U2.git
cd predictor-medico-mlops-U2
```

### 2. Ejecutar localmente con Docker

Asegúrate de tener Docker instalado y en ejecución:

```bash
docker build -t predictor-medico .
docker run -p 5000:5000 predictor-medico
```

Accede a la aplicación en: [http://localhost:5000](http://localhost:5000)

### 3. Usar imagen desde GitHub Container Registry (GHCR)

También puedes usar directamente la imagen publicada en GHCR:

```bash
docker run -p 8000:5000 ghcr.io/dannaaespinosa/predictor-medico-mlops-u2:latest
```

🔁 Cambia `8000` por el puerto que prefieras en tu máquina local.

---

## ✅ CI/CD con GitHub Actions

Cada vez que haces push a la rama `main`, se activa un workflow que:

1. Ejecuta pruebas unitarias (`pytest`)
2. Construye la imagen Docker
3. La publica automáticamente en [GHCR](https://ghcr.io)

Workflow YAML: `.github/workflows/main.yml`
---
### Cambios:

1. **Nueva Categoría**: Se ha añadido la categoría **"ENFERMEDAD TERMINAL"** a la función de predicción.
2. **Reportes**: La aplicación ahora genera un reporte de las predicciones con estadísticas clave, como el número de predicciones por categoría, las últimas 5 predicciones y la fecha de la última predicción.
3. **Descarga de Reportes**: Los usuarios pueden ver los reportes en la web y también descargarlos en formato `.txt` para su posterior revisión.
---

## 🧪 Uso de la aplicación

1. Abre la página web en tu navegador.  
2. Ingresa **tres valores numéricos** que representen síntomas.  
3. Haz clic en **"Predecir"**.  
4. Verás un resultado con el estado estimado del paciente:

- `NO ENFERMO`  
- `ENFERMEDAD LEVE`  
- `ENFERMEDAD AGUDA`  
- `ENFERMEDAD CRÓNICA`
- `ENFERMEDAD TERMINAL`

---

## 🧠 Lógica de predicción (modelo simulado)

```python
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
    elif suma <= 400:
        return "ENFERMEDAD CRÓNICA"
    else:
        return "ENFERMEDAD TERMINAL"

```

---

---

## 📁 Estructura del repositorio

```plaintext
predictor-medico/
├── app.py                  # Aplicación Flask principal
├── predictor.py            # Lógica de predicción simulada
├── requirements.txt        # Dependencias del entorno
├── Dockerfile              # Definición de la imagen Docker
├── templates/
│   └── index.html          # Interfaz web para ingresar síntomas
├── static/
│   └── style.css           # Estilos de la aplicación
├── tests/
│   └── test_predictor.py  # Pruebas unitarias
|   └── test_reports.py   
|   └── conftest.py   
└── .github/
    └── workflows/ 
        └── deploy-on-main-workflow.yml  # Workflow de CI/CD con GitHub Actions
```
        └── pull-request-workflow.yml     # Workflow de CI/CD con GitHub Actions
```    

---

## 👩‍💻 Autora

Danna Espinosa

---