# 🩺 Predictor Médico – Proyecto MLOps


Este repositorio contiene un pipeline básico de MLOps que simula un sistema de predicción médica. A través de una interfaz web, el usuario puede ingresar tres valores clínicos numéricos y obtener un diagnóstico estimado. La lógica de predicción está contenida en un archivo Python y la aplicación está empaquetada en un contenedor Docker listo para su despliegue.


---


## 📌 Objetivo


Simular un modelo de predicción de enfermedades comunes y huérfanas a partir de tres síntomas como parte de una práctica de desarrollo MLOps end-to-end. El proyecto tiene como fin construir un flujo de trabajo reproducible y mantenible que abarque:


- Desarrollo local  
- Empaquetado y despliegue con Docker  
- Automatización del ciclo de vida del modelo  
- Control de versiones y documentación con GitHub


---


## 🚀 Instrucciones


### 1. Clonar el repositorio


```bash
git clone https://github.com/DannaAEspinosa/predictor-medico-mlops-U2.git
cd predictor-medico
```


### 2. Construir la imagen Docker


Asegúrate de tener Docker instalado y ejecutándose:


```bash
docker build -t predictor-medico .
```


### 3. Ejecutar el contenedor


```bash
docker run -p 5000:5000 predictor-medico
```


La aplicación estará disponible en:


```
http://localhost:5000
```


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
    else:
        return "ENFERMEDAD CRÓNICA"
```


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
└── static/
    └── style.css           # Estilos de la aplicación
```


---


## ✅ Requisitos


- Docker  
- Navegador web


---


## 👩‍💻 Autora


Danna Espinosa

