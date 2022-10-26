from django.shortcuts import *
from django.views.generic import *
from django.http import *
from datetime import datetime
from Core.HomePage.models import Visita
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

# para hacer uso de esta librería se necesita internte
import geocoder # para la ubicación de la visita 
import requests
#import folium # instalar para ver la ubicación en un mapa

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

        # INICIO Obtener el navegador
        agent = self.request.environ.get('HTTP_USER_AGENT')
        browser = httpagentparser.detect(agent)
        if not browser:
            browser = agent.split('/')[0]
        else:
            browser = browser['browser']['name'] 
        context['navegador'] = str(browser) # este si funciona belleza
        browser = str(self.request.user_agent.browser.family) + ' ' + str(self.request.user_agent.browser.version)
        # FIN Obtener navegador

        # INICIO obtener IP y Ubicación
        rq = geocoder.ip("me")
        context['IP'] = str(rq.ip)
        ip = str(rq.ip)
        context['ubicacion'] = str(rq.address) +' / Latitud: '+ str(rq.lat) +' / Longitud: '+ str(rq.lng)
        ubicacion = str(rq.address) +' / Latitud: '+ str(rq.lat) +' / Longitud: '+ str(rq.lng)
        
        # FIN obtener IP y Ubicación

        dispositivo = ""
        #context['so'] = str(self.request.headers['User-Agent'])
        if self.request.user_agent.is_pc:
            dispositivo = "PC"
        else:
            if self.request.user_agent.is_mobile:
                dispositivo = "Celular"
            else:
                if self.request.user_agent.is_tablet:
                    dispositivo = "Tablet"
                else:
                    if self.request.user_agent.is_bot:
                        dispositivo = "Robot"

        so = str(self.request.user_agent.os.family) +' '+ str(self.request.user_agent.os.version) 
        context['so'] = so

        #context['so'] = str(self.request.user_agent.device)
        context['so'] = str(self.request.user_agent.device.family)

        # INICIO Generando Slug
        a=str(uuid.uuid4())
        b=str(datetime.now()).replace('-','').replace(':','').replace('.','-').replace(' ','-')
        c=random.choice(["a26", "31b", "98c", "d32", "11e", "f09", "28g"]) + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") + str(random.randint(1, 500))
        slug = random.choice("!&%#|£“¡¬-+}{ñ*$-())^~,_:¿?") + a + '-' + b + '-' + c
        # FIN Generando Slug

        self.guardarVisita(ip,ubicacion,dispositivo,browser,so,slug)

        return context
    
    