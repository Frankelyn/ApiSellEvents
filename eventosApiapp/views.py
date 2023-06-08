from urllib import request
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Evento
from .models import boleta
from django.core.exceptions import ObjectDoesNotExist
import json
from django.http import HttpResponse


@csrf_exempt
def get_eventos(request):
    if request.method == 'GET':
        eventos = Evento.objects.all()

        eventos_data = []
        for evento in eventos:
            evento_data = {
                'nombreEvento'      : evento.nombreEvento,
                'descripcionEvento' : evento.descripcionEvento,
                'fechaInicioEvento' : evento.fechaInicioEvento,
                'fechaFinEvento'    : evento.fechaFinEvento,
                'horaInicioEvento'  : evento.horaInicioEvento,
                'horaFinEvento'     : evento.horaFinEvento,
                'lugarEvento'       : evento.lugarEvento,
                'fotoPromoEvento'   : evento.fotoPromoEvento,
                'capacidadGeneral'  : evento.capacidadGeneral,
                'capacidadVip'      : evento.capacidadVip,
                'capacidadSuperVip' : evento.capacidadSuperVip
            }
            eventos_data.append(evento_data)

        return JsonResponse(eventos_data, safe=False)

@csrf_exempt
def post_evento(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            
            nombreEvento        = data.get('nombreEvento')
            descripcionEvento   = data.get('descripcionEvento')
            fechaInicioEvento   = data.get('fechaInicioEvento')
            fechaFinEvento      = data.get('fechaFinEvento')
            horaInicioEvento    = data.get('horaInicioEvento')
            horaFinEvento       = data.get('horaFinEvento')
            lugarEvento         = data.get('lugarEvento')
            fotoPromoEvento     = data.get('fotoPromoEvento')
            capacidadGeneral    = data.get('capacidadGeneral')
            capacidadVip        = data.get('capacidadVip')
            capacidadSuperVip   = data.get('capacidadSuperVip')

            evento = Evento(
                nombreEvento        = nombreEvento,
                descripcionEvento   = descripcionEvento,
                fechaInicioEvento   = fechaInicioEvento,
                fechaFinEvento      = fechaFinEvento,
                horaInicioEvento    = horaInicioEvento,
                horaFinEvento       = horaFinEvento,
                lugarEvento         = lugarEvento,
                fotoPromoEvento     = fotoPromoEvento,
                capacidadGeneral    = capacidadGeneral,
                capacidadVip        = capacidadVip,
                capacidadSuperVip   = capacidadSuperVip
            )
            evento.save()

            return JsonResponse({'mensaje': 'Evento creado con exito'})

        nombreEvento            = request.POST.get('nombreEvento')
        descripcionEvento       = request.POST.get('descripcionEvento')
        fechaInicioEvento       = request.POST.get('fechaInicioEvento')
        fechaFinEvento          = request.POST.get('fechaFinEvento')
        horaInicioEvento        = request.POST.get('horaInicioEvento')
        horaFinEvento           = request.POST.get('horaFinEvento')
        lugarEvento             = request.POST.get('lugarEvento')
        fotoPromoEvento         = request.POST.get('fotoPromoEvento')
        capacidadGeneral        = request.POST.get('capacidadGeneral')
        capacidadVip            = request.POST.get('capacidadVip')
        capacidadSuperVip       = request.POST.get('capacidadSuperVip')

        evento = Evento(
            nombreEvento        = nombreEvento,
            descripcionEvento   = descripcionEvento,
            fechaInicioEvento   = fechaInicioEvento,
            fechaFinEvento      = fechaFinEvento,
            horaInicioEvento    = horaInicioEvento,
            horaFinEvento       = horaFinEvento,
            lugarEvento         = lugarEvento,
            fotoPromoEvento     = fotoPromoEvento,
            capacidadGeneral    = capacidadGeneral,
            capacidadVip        = capacidadVip,
            capacidadSuperVip   = capacidadSuperVip
        )
        evento.save()

        return JsonResponse({'mensaje': 'Evento creado con exito'})


@csrf_exempt
def put_evento(request, evento_id):
    try:
        evento = Evento.objects.get(id=evento_id)
    except ObjectDoesNotExist:
        return JsonResponse({'mensaje': 'El evento no existe'}, status=404)

    if request.method == 'PUT':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            
            evento.nombreEvento         = data.get('nombreEvento')
            evento.descripcionEvento    = data.get('descripcionEvento')
            evento.fechaInicioEvento    = data.get('fechaInicioEvento')
            evento.fechaFinEvento       = data.get('fechaFinEvento')
            evento.horaInicioEvento     = data.get('horaInicioEvento')
            evento.horaFinEvento        = data.get('horaFinEvento')
            evento.lugarEvento          = data.get('lugarEvento')
            evento.fotoPromoEvento      = data.get('fotoPromoEvento')
            evento.capacidadGeneral     = data.get('capacidadGeneral')
            evento.capacidadVip         = data.get('capacidadVip')
            evento.capacidadSuperVip    = data.get('capacidadSuperVip')
            evento.save()

            return JsonResponse({'mensaje': 'El evento se ha actualizado con exito'})

        nombreEvento        = request.PUT.get('nombreEvento')
        descripcionEvento   = request.PUT.get('descripcionEvento')
        fechaInicioEvento   = request.PUT.get('fechaInicioEvento')
        fechaFinEvento      = request.PUT.get('fechaFinEvento')
        horaInicioEvento    = request.PUT.get('horaInicioEvento')
        horaFinEvento       = request.PUT.get('horaFinEvento')
        lugarEvento         = request.PUT.get('lugarEvento')
        fotoPromoEvento     = request.PUT.get('fotoPromoEvento')
        capacidadGeneral    = request.PUT.get('capaciadGeneral')
        capacidadVip        = request.PUT.get('capacidadVip')
        capacidadSuperVip   = request.PUT.get('capaciadSuperVip')

        evento.nombreEvento         = nombreEvento
        evento.descripcionEvento    = descripcionEvento
        evento.fechaInicioEvento    = fechaInicioEvento
        evento.fechaFinEvento       = fechaFinEvento
        evento.horaInicioEvento     = horaInicioEvento
        evento.horaFinEvento        = horaFinEvento
        evento.lugarEvento          = lugarEvento
        evento.fotoPromoEvento      = fotoPromoEvento
        evento.capacidadGeneral     = capacidadGeneral
        evento.capacidadVip         = capacidadVip
        evento.capacidadSuperVip    = capacidadSuperVip
        evento.save()

        return JsonResponse({'mensaje': 'El evento se ha actualizado con exito'})


@csrf_exempt
def delete_evento(request, evento_id):
    try:
        evento = Evento.objects.get(id=evento_id)
    except ObjectDoesNotExist:
        return JsonResponse({'mensaje': 'El evento no existe'}, status=404)

    if request.method == 'DELETE':
        evento.delete()

        return JsonResponse({'mensaje': 'Evento eliminado exitosamente'})


@csrf_exempt
def get_boletas(request):
    if request.method == 'GET':
        boletas = boleta.objects.all()

        boletas_data = []
        for _boleta in boletas:
            boleta_data = {
                'codigoBoleta': _boleta.codigoBoleta,
                'tipoBoleta': _boleta.tipoBoleta,
                'precioBoleta': _boleta.precioBoleta,
                'beneficiosBoleta': _boleta.beneficiosBoleta,
                'estadoBoleta': _boleta.estadoBoleta,
                'evento': _boleta.evento_id  # Accede al ID del evento
            }
            boletas_data.append(boleta_data)

        return JsonResponse(boletas_data, safe=False)



@csrf_exempt
def post_boleta(request):
    if request.method == 'POST':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            
            codigoBoleta = data.get('codigoBoleta')
            tipoBoleta = data.get('tipoBoleta')
            precioBoleta = data.get('precioBoleta')
            beneficiosBoleta = data.get('beneficiosBoleta')
            estadoBoleta = data.get('estadoBoleta')
            evento_id = data.get('evento')

            try:
                evento = Evento.objects.get(id=evento_id)
            except Evento.DoesNotExist:
                return JsonResponse({'mensaje': 'El evento no existe'}, status=404)

            _boleta = boleta(
                codigoBoleta=codigoBoleta,
                tipoBoleta=tipoBoleta,
                precioBoleta=precioBoleta,
                beneficiosBoleta=beneficiosBoleta,
                estadoBoleta=estadoBoleta,
                evento=evento
            )
            _boleta.save()

            return JsonResponse({'mensaje': 'Boleta creada con exito'})

        codigoBoleta = request.POST.get('codigoBoleta')
        tipoBoleta = request.POST.get('tipoBoleta')
        precioBoleta = request.POST.get('precioBoleta')
        beneficiosBoleta = request.POST.get('beneficiosBoleta')
        estadoBoleta = request.POST.get('estadoBoleta')
        evento_id = request.POST.get('evento')

        try:
            evento = Evento.objects.get(id=evento_id)
        except Evento.DoesNotExist:
            return JsonResponse({'mensaje': 'El evento no existe'}, status=404)

        _boleta = boleta(
            codigoBoleta=codigoBoleta,
            tipoBoleta=tipoBoleta,
            precioBoleta=precioBoleta,
            beneficiosBoleta=beneficiosBoleta,
            estadoBoleta=estadoBoleta,
            evento=evento
        )
        _boleta.save()

        return JsonResponse({'mensaje': 'Boleta creada con éxito'})


@csrf_exempt
def put_boleta(request, boleta_id):
    try:
        _boleta = boleta.objects.get(id=boleta_id)
    except ObjectDoesNotExist:
        return JsonResponse({'mensaje': 'La boleta no existe'}, status=404)

    if request.method == 'PUT':
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            
            _boleta.codigoBoleta     = data.get('codigoBoleta')
            _boleta.tipoBoleta       = data.get('tipoBoleta')
            _boleta.precioBoleta     = data.get('precioBoleta')
            _boleta.beneficiosBoleta = data.get('beneficiosBoleta')
            _boleta.estadoBoleta     = data.get('estadoBoleta')
            evento_id                = data.get('evento')

            try:
                evento = Evento.objects.get(id=evento_id)
                _boleta.evento = evento
            except Evento.DoesNotExist:
                return JsonResponse({'mensaje': 'El evento no existe'}, status=404)

            _boleta.save()

            return JsonResponse({'mensaje': 'La boleta se ha actualizado con éxito'})

        codigoBoleta        = request.PUT.get('codigoBoleta')
        tipoBoleta          = request.PUT.get('tipoBoleta')
        precioBoleta        = request.PUT.get('precioBoleta')
        beneficiosBoleta    = request.PUT.get('beneficiosBoleta')
        estadoBoleta        = request.PUT.get('estadoBoleta')
        evento_id           = request.PUT.get('evento')

        try:
            evento = Evento.objects.get(id=evento_id)
            _boleta.evento = evento
        except Evento.DoesNotExist:
            return JsonResponse({'mensaje': 'El evento no existe'}, status=404)

        _boleta.codigoBoleta     = codigoBoleta
        _boleta.tipoBoleta       = tipoBoleta
        _boleta.precioBoleta     = precioBoleta
        _boleta.beneficiosBoleta = beneficiosBoleta
        _boleta.estadoBoleta     = estadoBoleta
        _boleta.save()

        return JsonResponse({'mensaje': 'Boleta eliminada exitosamente'})


@csrf_exempt
def delete_boletas(request, boleta_id):
    try:
        _boleta = boleta.objects.get(id=boleta_id)
    except ObjectDoesNotExist:
        return JsonResponse({'mensaje': 'La boleta no existe'}, status=404)

    if request.method == 'DELETE':
        _boleta.delete()

        return JsonResponse({'mensaje': 'Boleta eliminada exitosamente'})


# Create your views here.
