from django.shortcuts import render
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



class HomePageView(TemplateView):
    #model= visitas
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['demo'] = 'Demo'
        #context['hostname'] = str(socket.gethostname()) 
        #context['IP'] = str(socket.gethostbyname(socket.gethostname()))
        #context['navegador'] = str(socket.gethostbyname("www.google.com"))

        # Obtener el navegador
        agent = self.request.environ.get('HTTP_USER_AGENT')
        browser = httpagentparser.detect(agent)
        if not browser:
            browser = agent.split('/')[0]
        else:
            browser = browser['browser']['name'] 
        #FIN Obtener navegador

        context['navegador'] = str(browser) # este si funciona belleza
        #context['navegador2'] = str(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))


        #s = "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.9 (KHTML, like Gecko) \
        #Chrome/5.0.307.11 Safari/532.9"
        #context['navegador3'] = str(httpagentparser.simple_detect(s))
        #context['navegador3'] = str(httpagentparser.detect(s))

        #s = "Mozilla/5.0 (Linux; U; Android 2.3.5; en-in; HTC_DesireS_S510e Build/GRJ90) \
        #        AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
        #context['navegador3'] = str(httpagentparser.simple_detect(s))
        #context['navegador3'] = str(httpagentparser.detect(s))

        #st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #try:       
        #    st.connect(('10.255.255.255', 1))
        #    IP = st.getsockname()[0]
        #except Exception:
        #    IP = '127.0.0.1'
        #finally:
        #    st.close()
   
        #context['IP'] = str(IP) #dejarlo pero es local 
        #context['IP2'] = str(socket.gethostbyname_ex(socket.gethostname())) #dejarlo pero es local 
        
        #geolocator = Nominatim(user_agent="carteaga")
        rq = geocoder.ip("me")
        context['IP'] = str(rq.ip)
        context['ubicacion'] = str(rq.address) +' / Latitud: '+ str(rq.lat) +' / Longitud: '+ str(rq.lng)
        #context['ubicacion'] = str(rq.json)
        #context['ubicacion'] = str(rq.json)

        context['so'] = str(socket.gethostbyname(socket.gethostname()) + socket.gethostname())
        return context

#class DatosVisitaView(TemplateView):
    