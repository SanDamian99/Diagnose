import streamlit as st
import time
import random
# Se importa la librería de Gemini para ilustrar el uso de la API (según el ejemplo)
import google.generativeai as genai

# ----- Configuración y simulación del uso de la API de Gemini -----
api_keys = [
    "AIzaSyDKzApq_jz4gOJJYG_PbBwc47Lw96FxHAY",
    "AIzaSyBTnhTp46S7svZ1olGEpwH1i3XlZ4B4kMA",
    "AIzaSyAEaxnxgoMXwg9YVRmRH_tKVGD3pNgHKkk",
    "AIzaSyDnPvhKe0XVAj3QpS9tu52A_hwjjrpAFEs",
    "AIzaSyDFR3EE31lRiwV5i6LbMNKQVIoinQlgjSs"
]
current_api_key_index = 0

def configure_api():
    global current_api_key_index
    genai.configure(api_key=api_keys[current_api_key_index])
    
configure_api()

def create_text_model():
    # Configuración simplificada para el modelo de texto
    text_generation_config = {
        "temperature": 0.4,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 8000,
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
    ]
    return genai.GenerativeModel(model_name="gemini-2.0-flash",
                                  generation_config=text_generation_config,
                                  safety_settings=safety_settings)

text_model = create_text_model()

# Función simulada para generar actividades de comparación de fracciones.
def generate_exercises(objective, correct_example):
    # En un escenario real se invocaría a Gemini para generar ejercicios dinámicamente.
    activities = [
        "Actividad 1: Dada la comparación de fracciones, determina cuál es mayor: 3/4 vs 2/3",
        "Actividad 2: Ordena las siguientes fracciones de menor a mayor: 1/2, 3/5, 2/3",
        "Actividad 3: Compara y di si es verdadero o falso: 5/8 > 4/7"
    ]
    return activities

# Función de evaluación simple para clasificar el desempeño del estudiante.
def classify_student(responses):
    # Se utiliza una lógica muy simple basada en la cantidad de palabras en las respuestas.
    total_words = sum(len(resp.split()) for resp in responses)
    if total_words >= 50:
        return "Excelente"
    elif total_words >= 30:
        return "Bueno"
    elif total_words >= 15:
        return "Regular"
    else:
        return "Deficiente"

# Función principal de la aplicación Streamlit.
def main():
    st.title("Diagnose Math")
    
    # Sección de Objetivo de Aprendizaje
    st.header("Objetivo de Aprendizaje")
    learning_objective = "Comparar fracciones para identificar cuál es mayor y cuál es menor"
    st.write(learning_objective)
    
    # Sección de Ejemplo de Desempeño Correcto
    st.header("Ejemplo de Desempeño Correcto")
    correct_example = ("Ejemplo: Para comparar 3/4 y 2/3 se convierte a un denominador común o se realiza la división. "
                       "Observando que 0.75 > 0.66, se concluye que 3/4 es mayor.")
    st.write(correct_example)
    
    # Sección de la primera explicación visual (solo el enunciado)
    st.header("Primera Explicación Visual")
    st.write("Enunciado: Visualizar las fracciones en una recta numérica para identificar sus posiciones relativas.")
    
    # Generación de actividades (simulando el uso de la API de Gemini)
    st.header("Actividades")
    activities = generate_exercises(learning_objective, correct_example)
    for act in activities:
        st.write(act)
    
    # Formulario para que el estudiante ingrese sus respuestas
    st.header("Ingreso de Respuestas del Estudiante")
    student_responses = []
    for idx, act in enumerate(activities):
        response = st.text_area(f"Ingrese su respuesta para la {act}", key=f"resp_{idx}")
        student_responses.append(response)
    
    # Botón para evaluar el desempeño y generar la clasificación
    if st.button("Evaluar Desempeño"):
        classification = classify_student(student_responses)
        st.success(f"Clasificación del Estudiante: {classification}")
        st.info("Esta clasificación es enviada, en teoría, al profesor.")

if __name__ == '__main__':
    main()
