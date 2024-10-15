from flask import Flask, request, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    domicilio = request.form['domicilio']
    estado = request.form['estado']
    edad = request.form['edad']
    sexo = request.form['sexo']
    tipo_cedula = request.form['tipo_cedula']
    correo = request.form['correo']
    celular = request.form['celular']
    experiencia = request.form['experiencia']
    cv = request.files['cv']

    # Configurar el envío de correo
    sender_email = 'testformulario1@outlook.com'  # Cambia esto
    receiver_email = 'usuariotinker12@gmail.com'  # Cambia esto
    password = 'Testprueba12#'  # Cambia esto

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Nueva Solicitud de Contratación'

    body = f"""Nombre: {nombre}
Domicilio: {domicilio}
Estado: {estado}
Edad: {edad}
Sexo: {sexo}
Tipo de Cédula: {tipo_cedula}
Correo Electrónico: {correo}
Celular: {celular}
Experiencia: {experiencia}
"""
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el CV
    if cv:
        attachment = MIMEApplication(cv.read(), _subtype='pdf')
        attachment.add_header('Content-Disposition', 'attachment', filename=cv.filename)
        msg.attach(attachment)

    # Enviar el correo
    try:
        with smtplib.SMTP('smtp.outlook.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        return "Formulario enviado con éxito."
    except Exception as e:
        return f"Error al enviar el formulario: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
