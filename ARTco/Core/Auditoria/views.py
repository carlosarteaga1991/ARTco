from django.shortcuts import render
from django.shortcuts import *
from django.views.generic import *
from django.http import *
from datetime import datetime
from Core.Auditoria.models import log
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

class Generar_log(CreateView):
    model= log
    error = ""

    # Guardando datos de la visita 
    def guardar_log(self,pantalla_afectada,DB_afectada,tabla_afectada,campo_afectado,id_registro_afectado,id_usuario,accion,estado,dato_viejo,dato_nuevo,otra_accion):
        try:
            rq = geocoder.ip("me")
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
            registro = log(
                ip = str(rq.ip),
                ubicacion = str(rq.address) +' / Latitud: '+ str(rq.lat) +' / Longitud: '+ str(rq.lng),
                dispositivo = dispositivo,
                navegador = str(self.request.user_agent.browser.family) + ' ' + str(self.request.user_agent.browser.version),
                sistemaoperativo = str(self.request.user_agent.os.family) +' '+ str(self.request.user_agent.os.version) ,
                pantalla_afectada = str(pantalla_afectada),
                DB_afectada = str(DB_afectada),
                tabla_afectada = str(tabla_afectada),
                campo_afectado = str(campo_afectado),
                id_registro_afectado = int(id_registro_afectado),
                id_usuario = int(id_usuario),
                accion = str(accion),
                estado = str(estado),
                dato_viejo = str(dato_viejo),
                dato_nuevo = str(dato_nuevo),
                otra_accion = str(otra_accion)
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

        return context
