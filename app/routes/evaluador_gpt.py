from openai import OpenAI

client = OpenAI(api_key=tu_api_key)

def evaluar_candidato(texto_cv, descripcion_oferta):
    try:
        prompt = f"""Dada la siguiente descripción de una oferta laboral:

{descripcion_oferta}

Y el siguiente texto de un currículum:

{texto_cv}

Evalúa qué tan bien se ajusta el candidato a la oferta. Devuelve un breve análisis con una puntuación de 1 a 10.
"""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un evaluador de recursos humanos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al evaluar candidato: {str(e)}"
