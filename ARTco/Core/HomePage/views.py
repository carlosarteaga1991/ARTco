from ensurepip import version
from django.shortcuts import *
from django.views.generic import *
from django.http import *
from datetime import datetime
from Core.HomePage.models import Visita
from Conf.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, DOMAIN
from django.shortcuts import *

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.urls import reverse_lazy
import uuid
import random

import socket
import httpagentparser
from geopy.geocoders import Nominatim

from Core.Auditoria.views import *

# para hacer uso de esta librería se necesita internte
import geocoder # para la ubicación de la visita 
import requests
#import folium # instalar para ver la ubicación en un mapa

# Para envío de correo
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string

# Para mensajes de django
from django.contrib.messages import *


import platform

class HomePageView(TemplateView):
    model= Visita
    template_name = 'index.html'
    error = ""

    # Guardando datos de la visita 
    def guardarVisita(self,ip,ubicacion,dispositivo,navegador,so,slug):
        try:
            registro = Visita(
                ip_visita = str(ip),
                ubicacion_visita = str(ubicacion),
                dispositivo_visitante = str(dispositivo),
                navegador = str(navegador),
                sistema_operativo = str(so),
                slog_visita = slug
            )
            registro.save()
        except Exception as e:
            error = "Se presentó un error al guardar"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'
        context['error'] = self.error
        context['homepage_url']= reverse_lazy('HomePage:homepage')
        context['politicaPrivacidad_url']= reverse_lazy('HomePage:politicaPrivacidad')

        # INICIO Obtener el navegador
        agent = self.request.environ.get('HTTP_USER_AGENT')
        browser = httpagentparser.detect(agent)
        if not browser:
            browser = agent.split('/')[0]
        else:
            browser = browser['browser']['name'] 
        browser = str(self.request.user_agent.browser.family) + ' ' + str(self.request.user_agent.browser.version)
        # FIN Obtener navegador

        # INICIO obtener IP y Ubicación
        rq = geocoder.ip("me")
        context['IP'] = str(rq.ip)
        ip = str(rq.ip)
        ubicacion = str(rq.address) +' / Latitud: '+ str(rq.lat) +' / Longitud: '+ str(rq.lng)
        
        # FIN obtener IP y Ubicación

        dispositivo = ""
        #context['so'] = str(self.request.headers['User-Agent'])
        if self.request.user_agent.is_pc:
            dispositivo = "PC"
        else:
            if self.request.user_agent.is_mobile:
                dispositivo = "Móvil"
            else:
                if self.request.user_agent.is_tablet:
                    dispositivo = "Tablet"
                else:
                    if self.request.user_agent.is_bot:
                        dispositivo = "Robot"

        so = str(self.request.user_agent.os.family) +' '+ str(self.request.user_agent.os.version) 

        #context['so'] = str(self.request.user_agent.device) 

        # INICIO Generando Slug
        a=str(uuid.uuid4())
        b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
        c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
        slug = random.choice("!&%#|£“¡¬-+}{ñ*$-())^~,_:¿?") + a + '-' + b + '-' + c
        # FIN Generando Slug

        self.guardarVisita(ip,ubicacion,dispositivo,browser,so,slug)

        return context
    
    # Para envío de correo de Contacto POST
    def post(self, request, *args, **kwargs):
        data = {}
        exitoso = False
        fallido = False
        if self.request.POST['action'] == 'contacto':
            #data['name'] = self.request.POST['name']
            nombre = self.request.POST['name']
            email_dest = self.request.POST['email']
            asunto_dest = self.request.POST['subject']
            mensaje_dest = self.request.POST['message']
            otra_accion = str("Se envió correo de contacto a: " + self.request.POST['name'] + ", al email: " + self.request.POST['email'])
                
            #self.enviar_email(email_dest)
            # INICIO envío de correo
            try:
                # Para obtener el dominio completo 
                URL = DOMAIN if not DEBUG else self.request.META['HTTP_HOST']
                mailServer = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
                print(mailServer.ehlo()) # Para ver si hay conexión
                mailServer.starttls()
                print(mailServer.ehlo()) # Para ver si hay conexión
                mailServer.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
                email_to = email_dest
                mensaje = MIMEMultipart()
                #mensaje = MIMEText("este es una prueba")
                mensaje['From'] = EMAIL_HOST_USER
                mensaje['To'] = email_to
                mensaje['Subject'] = 'Info - Arteaga | Corporación'

                content = render_to_string('contacto_correo.html', {
                    'usuario': nombre,
                    #'link_resetpwd': 'http://{}/login/cambiar/contrasenia/{}/'.format(URL, str(email)),
                    'link_home': ''
                })
                #content = "prueba enduro"
                mensaje.attach(MIMEText(content, 'html'))
                        #autenticación de doble factot

                mailServer.sendmail(EMAIL_HOST_USER,
                                    email_to,
                                    mensaje.as_string())
                Generar_log.guardar_log(self,'HomePage/Contacto','No Aplica','No Aplica','No Aplica',0,0,'Envío de Correo','Exitoso','No Aplica','No Aplica',otra_accion)
            
            except Exception as e:
                data['fallido'] = "Se ha producido un error"
                Generar_log.guardar_log(self,'HomePage/Contacto','No Aplica','No Aplica','No Aplica',0,0,'Envío de Correo','Fallido','No Aplica','No Aplica',otra_accion)
                data['error'] = str(e)
            # FIN envío de correo

        return JsonResponse(data)

class PoliticaPrivacidadView(TemplateView):
    template_name = 'Politica_privacidad.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'
        context['homepage_url']= reverse_lazy('HomePage:homepage')
        return context