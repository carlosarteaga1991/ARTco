from django.shortcuts import *
from django.views.generic import *
from django.http import *
from datetime import datetime
from Core.HomePage.models import visitas
from django.shortcuts import *

import socket
import httpagentparser
from geopy.geocoders import Nominatim

# para hacer uso de esta librería se necesita internte
import geocoder # para la ubicación de la visita 
import requests
#import folium # instalar para ver la ubicación en un mapa

import platform





class HomePageView(TemplateView):
    #model= visitas
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'

        # INICIO Obtener el navegador
        agent = self.request.environ.get('HTTP_USER_AGENT')
        browser = httpagentparser.detect(agent)
        if not browser:
            browser = agent.split('/')[0]
        else:
            browser = browser['browser']['name'] 
        context['navegador'] = str(browser) # este si funciona belleza
        # FIN Obtener navegador

        # INICIO obtener IP y Ubicación
        rq = geocoder.ip("me")
        context['IP'] = str(rq.ip)
        context['ubicacion'] = str(rq.address) +' / Latitud: '+ str(rq.lat) +' / Longitud: '+ str(rq.lng)
        # FIN obtener IP y Ubicación

        #str(socket.gethostbyname(socket.gethostname()) + socket.gethostname())
        #str(platform.system()) + '/ '+ str(platform.release()) + '/ '+ str(platform.version())
        #HttpRequest.META('HTTP_USER_AGENT')
        context['so'] = str(self.request.headers['User-Agent'])
        return context

    