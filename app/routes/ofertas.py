# app/routes/ofertas.py
from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app import db
from app.models import OfertaLaboral
from app.utils.gmail_utils import contar_correos_por_asunto, obtener_adjuntos_pdf, get_authenticated_service, buscar_mensajes_por_asunto
from app.utils.pdf_utils import extraer_texto_pdf
from app.routes.evaluador import evaluar_candidato

ofertas = Blueprint('ofertas', __name__, url_prefix='/ofertas')

@ofertas.route('/', methods=['GET'])
def listar_ofertas():
    keyword = request.args.get('keyword', '').lower()
    if keyword:
        # Buscar coincidencias en titulo, ciudad, objetivo, requisitos, habilidades
        ofertas = OfertaLaboral.query.filter(
            (OfertaLaboral.titulo.ilike(f'%{keyword}%')) |
            (OfertaLaboral.ciudad.ilike(f'%{keyword}%')) |
            (OfertaLaboral.objetivo.ilike(f'%{keyword}%')) |
            (OfertaLaboral.requisitos.ilike(f'%{keyword}%')) |
            (OfertaLaboral.habilidades.ilike(f'%{keyword}%'))
        ).all()
    else:
        ofertas = OfertaLaboral.query.all()

    resultado = []
    for o in ofertas:
        resultado.append({
            'id': o.id,
            'titulo': o.titulo,
            'ciudad': o.ciudad,
            'objetivo': o.objetivo,
            'requisitos': o.requisitos,
            'habilidades': o.habilidades,
            'correo_contacto': o.correo_contacto,
            'asunto_correo': o.asunto_correo
        })
    return render_template('listar_ofertas.html', ofertas=ofertas)


@ofertas.route('/crear', methods=['GET', 'POST'])
def crear_oferta():
    if request.method == 'POST':
        # Obtener datos desde el formulario HTML
        titulo = request.form.get('titulo')
        ciudad = request.form.get('ciudad')
        objetivo = request.form.get('objetivo')
        requisitos = request.form.get('requisitos')
        habilidades = request.form.get('habilidades')
        correo_contacto = request.form.get('correo_contacto')
        asunto_correo = request.form.get('asunto_correo')

        # Validar campos requeridos
        if not all([titulo, ciudad, objetivo, requisitos, habilidades, correo_contacto, asunto_correo]):
            return "Faltan datos obligatorios", 400

        # Crear y guardar la oferta
        nueva_oferta = OfertaLaboral(
            titulo=titulo,
            ciudad=ciudad,
            objetivo=objetivo,
            requisitos=requisitos,
            habilidades=habilidades,
            correo_contacto=correo_contacto,
            asunto_correo=asunto_correo
        )
        db.session.add(nueva_oferta)
        db.session.commit()

        return redirect(url_for('ofertas.listar_ofertas'))

    # Si es GET, mostrar el formulario
    return render_template('crear_oferta.html')


@ofertas.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_oferta(id):
    oferta = OfertaLaboral.query.get_or_404(id)
    
    if request.method == 'POST':
        oferta.titulo = request.form['titulo']
        oferta.ciudad = request.form['ciudad']
        oferta.objetivo = request.form['objetivo']
        oferta.requisitos = request.form['requisitos']
        oferta.habilidades = request.form['habilidades']
        oferta.correo_contacto = request.form['correo_contacto']
        oferta.asunto_correo = request.form['asunto_correo']
        
        db.session.commit()
        return redirect(url_for('ofertas.listar_ofertas'))

    return render_template('editar_oferta.html', oferta=oferta)

@ofertas.route('/<int:id>', methods=['DELETE'])
def eliminar_oferta(id):
    oferta = OfertaLaboral.query.get_or_404(id)
    db.session.delete(oferta)
    db.session.commit()

    return jsonify({'mensaje': 'Oferta eliminada'})

@ofertas.route('/ofertas/<int:id>/estadisticas', endpoint='ver_estadisticas')
def ver_estadisticas(id):
    oferta = OfertaLaboral.query.get_or_404(id)

    # Usar el título como el asunto a buscar
    asunto = oferta.asunto_correo
    cantidad_correos = contar_correos_por_asunto(asunto)

    return render_template(
        'estadisticas_oferta.html',
        oferta=oferta,
        asunto=asunto,
        cantidad_correos=cantidad_correos
    )

@ofertas.route('/ofertas/<int:id>/informe', methods=['GET'], endpoint='generar_informe')
def generar_informe(id):
    oferta = OfertaLaboral.query.get_or_404(id)
    asunto = oferta.asunto_correo

    descripcion = f"""
{oferta.titulo}
{oferta.ciudad}
Objetivo: {oferta.objetivo}

Requisitos: {oferta.requisitos}
Habilidades: {oferta.habilidades}

Contacto: {oferta.correo_contacto}
Asunto: {oferta.asunto_correo}
"""

    service = get_authenticated_service()
    mensajes = buscar_mensajes_por_asunto(service, asunto)
    
    evaluaciones = []

    for mensaje in mensajes:
        pdf_bytes = obtener_adjuntos_pdf(service, mensaje['id'])

        if pdf_bytes:
            texto_cv = extraer_texto_pdf(pdf_bytes)
            resultado = evaluar_candidato(texto_cv, descripcion)

            evaluaciones.append({
                "nombre": resultado["nombre"],
                "calificacion": resultado["calificacion"],
                "evaluacion": resultado["evaluacion"]
            })

    # Ordenar por calificación descendente
    mejores = sorted(evaluaciones, key=lambda x: x["calificacion"], reverse=True)[:3]

    return render_template(
        'informe_candidatos.html',
        oferta=oferta,
        evaluaciones=evaluaciones,
        mejores=mejores
    )
