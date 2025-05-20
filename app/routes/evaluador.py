import json
import re
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Esto carga las variables del archivo .env al entorno

# Luego accedes a ellas con os.getenv:


client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    base_url = os.getenv("OPENAI_BASE_URL"),
)

def evaluar_candidato(texto_cv, descripcion_oferta):
    try:
        prompt = f"""Dada la siguiente descripción de una oferta laboral:

{descripcion_oferta}

Y el siguiente texto de un currículum:

{texto_cv}

Evalúa qué tan bien se ajusta el candidato a la oferta. Devuelve una respuesta en formato JSON con estas claves exactas:
- "Nombre del candidato"
- "Calificación" (de 1 a 10)
- "Análisis" (máximo 100 palabras)
"""
        response = client.chat.completions.create(
            model="deepseek/deepseek-prover-v2:free",
            messages=[
                {"role": "system", "content": "Eres un evaluador de recursos humanos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        content = response.choices[0].message.content.strip()

        # Intentar extraer JSON con regex (en caso de que venga texto adicional)
        json_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group())
        else:
            raise ValueError("No se pudo extraer JSON")

        return {
            "nombre": data.get("Nombre del candidato", "Desconocido"),
            "calificacion": data.get("Calificación", 0),
            "evaluacion": data.get("Análisis", "No se pudo analizar correctamente.")
        }

    except Exception as e:
        return {
            "nombre": "Error",
            "calificacion": 0,
            "evaluacion": f"Error al evaluar candidato: {str(e)}"
        }
