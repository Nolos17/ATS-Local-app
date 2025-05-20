import fitz 


def extraer_texto_pdf(pdf_bytes):
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        texto = ""
        for pagina in doc:
            texto += pagina.get_text()
        return texto.strip()
