import os
from dotenv import load_dotenv
import os.path
import base64
from email import message_from_bytes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_authenticated_service():
    creds = None

    token_path = os.getenv('GOOGLE_TOKEN_PATH')
    credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH')

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def contar_correos_por_asunto(asunto_busqueda):
    service = get_authenticated_service()
    query = f'subject:"{asunto_busqueda}"'
    result = service.users().messages().list(userId='me', q=query).execute()
    mensajes = result.get('messages', [])

    conteo = 0
    for mensaje in mensajes:
        msg = service.users().messages().get(userId='me', id=mensaje['id'], format='metadata', metadataHeaders=['Subject']).execute()
        headers = msg.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '')

        # Comparación insensible a mayúsculas/minúsculas y exacta
        if subject.strip().lower() == asunto_busqueda.strip().lower():
            conteo += 1

    return conteo

def buscar_mensajes_por_asunto(service, asunto_busqueda):
    query = f'subject:"{asunto_busqueda}"'
    result = service.users().messages().list(userId='me', q=query).execute()
    mensajes = result.get('messages', [])

    mensajes_filtrados = []

    for mensaje in mensajes:
        msg = service.users().messages().get(userId='me', id=mensaje['id'], format='metadata', metadataHeaders=['Subject']).execute()
        headers = msg.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '')

        if subject.strip().lower() == asunto_busqueda.strip().lower():
            mensajes_filtrados.append({
                'id': mensaje['id'],
                'subject': subject
            })

    return mensajes_filtrados
def buscar_mensajes_por_asunto(service, asunto_busqueda):
    query = f'subject:"{asunto_busqueda}"'
    result = service.users().messages().list(userId='me', q=query).execute()
    mensajes = result.get('messages', [])

    mensajes_filtrados = []

    for mensaje in mensajes:
        msg = service.users().messages().get(userId='me', id=mensaje['id'], format='metadata', metadataHeaders=['Subject']).execute()
        headers = msg.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '')

        if subject.strip().lower() == asunto_busqueda.strip().lower():
            mensajes_filtrados.append({
                'id': mensaje['id'],
                'subject': subject
            })

    return mensajes_filtrados
def buscar_mensajes_por_asunto(service, asunto_busqueda):
    query = f'subject:"{asunto_busqueda}"'
    result = service.users().messages().list(userId='me', q=query).execute()
    mensajes = result.get('messages', [])

    mensajes_filtrados = []

    for mensaje in mensajes:
        msg = service.users().messages().get(userId='me', id=mensaje['id'], format='metadata', metadataHeaders=['Subject']).execute()
        headers = msg.get('payload', {}).get('headers', [])
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '')

        if subject.strip().lower() == asunto_busqueda.strip().lower():
            mensajes_filtrados.append({
                'id': mensaje['id'],
                'subject': subject
            })

    return mensajes_filtrados

def obtener_adjuntos_pdf(service, mensaje_id):
    mensaje = service.users().messages().get(userId='me', id=mensaje_id).execute()
    partes = mensaje.get("payload", {}).get("parts", [])
    
    for parte in partes:
        if parte.get("filename", "").endswith(".pdf"):
            adjunto_id = parte["body"]["attachmentId"]
            adjunto = service.users().messages().attachments().get(
                userId='me', messageId=mensaje_id, id=adjunto_id).execute()
            
            datos = base64.urlsafe_b64decode(adjunto["data"].encode("UTF-8"))
            return datos  # Retorna el contenido binario del PDF

    return None


