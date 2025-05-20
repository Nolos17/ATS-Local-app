# ATS Local

¡ATS Local es tu solución definitiva para gestionar ofertas laborales y automatizar la selección de talento con inteligencia artificial! 🚀 Esta aplicación Flask te permite administrar vacantes y seleccionar al mejor candidato mediante integración con el correo mediante la API de Gmail y análisis impulsado por IA. Diseñada para ser eficiente y moderna, es ideal para empresas que buscan optimizar su proceso de contratación. 🎨💻

## ✨ Características

📢 **Gestión de Ofertas Laborales**  
Crea y administra vacantes con facilidad:

- Publica nuevas ofertas laborales.
- Edita o elimina vacantes según las necesidades de la empresa.

📧 **Integración con Gmail API**  
Gestiona rapidamente todos tus correos de una vacante especifica:

- Identifica la cantidad de correos disponibles para una vacante en especifico.
- Procesa sus CV de forma automática.

🤖 **Selección Automatizada con IA**  
Identifica al mejor candidato automáticamente:

- Analiza currículums de los postulantes con algoritmos de IA.
- Identifica los mejores candidatos de manera rapida y optima.

🎨 **Diseño Modular**  
Código escalable y limpio, perfecto para personalizaciones.

## 🛠️ Tecnologías Usadas

⚡ **Flask**: Framework ligero para aplicaciones web en Python.  
📜 **SQLAlchemy**: ORM para gestión de bases de datos relacionales.  
🔑 **Google API Python Client**: Integración con la API de Gmail.  
🔒 **Flask-Login**: Gestión de autenticación y sesiones.  
🌐 **python-dotenv**: Carga de variables de entorno desde `.env`.  
📄 **PyMuPDF** y **pdfminer.six**: Procesamiento de PDFs.  
🐍 **Python**: Lógica principal y entorno de ejecución (3.10+).

## 📸 Capturas de Pantalla

**Panel de Ofertas Laborales** 🌐  
_Interfaz de ATS Local_  
Administra vacantes y candidatos desde un panel intuitivo.

**Selección de Candidatos** 🤖  
_Análisis de IA_  
Visualiza clasificaciones y selecciona al mejor candidato con un clic.

## 🔧 Instalación

Sigue estos pasos para instalar ATS Local en tu computadora :

### 📋 Requisitos

- 🐍 Python 3.10 o superior.
- 🔑 Archivo `credentials.json` de Google API.
- 🌐 Entorno virtual configurado.
- ⚙️ Archivo `.env` para variables de entorno.

### 📥 Pasos para Instalar

1. **Clonar el Repositorio**  
   Transfiere el proyecto a tu máquina:

   ```bash
   git clone https://github.com/tu-usuario/ats-local.git
   cd ats-local
   ```

2. **Crear Entorno Virtual**  
   Configura un entorno virtual para mantener las dependencias aisladas:

   ```bash
   python -m venv venv
   ```

3. **Activar Entorno Virtual**

   - En **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - En **Linux/Mac**:

     ```bash
     source venv/bin/activate
     ```

4. **Instalar Dependencias**  
   Instala todas las librerías necesarias:

   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar Variables de Entorno**  
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

   ```ini
    # Clave de OpenAI u OpenRouter
    OPENAI_API_KEY= tu_api_key
    OPENAI_BASE_URL=https://openrouter.ai/api/v1

    GOOGLE_CREDENTIALS_PATH=ruta_a_tu_archivo_credentials.json
    GOOGLE_TOKEN_PATH=ruta_a_tu_archivo_token.json_o_tu_token
   ```

6. **Agregar Credenciales de Google**  
   Coloca tu archivo `credentials.json` y token.json en la carpeta credentials.

7. **Ejecutar la Aplicación**  
   Inicia el servidor Flask:

   ```bash
   flask run
   ```

   La app estará disponible en `http://127.0.0.1:5000/`. 🎉

## 🚀 Para Desarrolladores: Modificar y Personalizar

¿Quieres personalizar ATS Local? Aquí tienes los pasos:

### 📋 Requisitos

- 🐍 Python 3.10 o superior.
- 🔧 Editor de código (recomendado: Visual Studio Code).
- 🌐 Sistema operativo compatible (Windows, macOS, Linux).

### 📦 Pasos

1. **Clonar o Copiar el Proyecto**  
   Si aún no lo hiciste, clona el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/ats-local.git
   cd ats-local
   ```

2. **Instalar Dependencias**  
   Asegúrate de tener las dependencias instaladas:

   ```bash
   pip install -r requirements.txt
   ```

3. **Modificar el Código**  
   Archivos clave:

   - `models.py`: Definiciones de modelos SQLAlchemy (candidatos, ofertas).
   - `routes/`: Rutas y endpoints para vacantes y candidatos.
   - `templates/`: Plantillas HTML para la interfaz.

4. **Probar Cambios**  
   Inicia la app en modo desarrollo:

   ```bash
   flask run
   ```

## 🎯 Instrucciones de Uso

📢 **Gestionar Ofertas Laborales**

- Crea una nueva vacante con detalles como título, descripción y requisitos.
- Edita o elimina vacantes desde el panel de administración.

🤖 **Seleccionar Candidatos**

- En base a los postulantes en el correo selecciona al mejor candidato.
- Usa la IA para clasificar candidatos según habilidades y experiencia.

📧 **Comunicar con Candidatos (Por implementar)**

- Envía correos automáticos para confirmar aplicaciones o programar entrevistas.
- Monitorea respuestas en el panel integrado con Gmail.

📊 **Gestionar Datos**

- Administra información de candidatos y vacantes en la base de datos.
- Genera reportes con estadísticas de selección.

🔒 **Autenticación**

- Inicia sesión como administrador para acceder al panel.
- Cierra sesión para proteger la cuenta.

🚪 **Cerrar la App**

- Detén el servidor Flask con `Ctrl+C` en la terminal.

## 🤝 Contribuir

¡Tus ideas son bienvenidas! 🌟 Para contribuir:

🍴 Haz un fork del repositorio.  
🌱 Crea una rama (`git checkout -b mi-caracteristica`).  
✍️ Realiza tus cambios y haz commit (`git commit -m "Añadir característica"`).  
🚀 Sube tu rama (`git push origin mi-caracteristica`).  
📬 Abre un Pull Request en GitHub.

Por favor, sigue el estilo del código y añade comentarios si es necesario.

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 📞 Soporte

¿Tienes problemas o sugerencias?

- Contacta al desarrollador: noloststorres@gmial.com.
- Abre un issue en el repositorio (si está en GitHub).

¡Disfruta optimizando la contratación con ATS Local! 📢✨
