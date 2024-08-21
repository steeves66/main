from django.http import HttpResponse
from django.shortcuts import render
from bien_immobiliers.models import *


def home(request):
    # bien vedette
    product_vedette = Bien.objects.filter(featured=True,visible=True).order_by('date_ajout')[:4]

    # bien location
    product_location = Bien.objects.filter(type_bien='msn', visible=True, mode_commercial__code__exact='loc').order_by('date_ajout')[:9]

    # bien location
    product_vente = Bien.objects.filter(type_bien='msn', visible=True, mode_commercial__code__exact='vnt').order_by('date_ajout')[:9]

    # biens immobiliers
    product_immobiliers = Bien.objects.filter(type_bien='msn', promotion_immobiliere=True).order_by('-date_ajout')[:4]

    # temoignages
    temoignages = Temoignage.objects.all().order_by('-date_creation')[:3]

    # entreprise branding
    brandings = Depositaire.objects.all().values('branding_images').order_by('-date_creation')[:6]

    context = {
            'product_vedette': product_vedette,
            'product_location': product_location,
            'product_vente': product_vente,
            'product_immobiliers': product_immobiliers,
            'temoignages': temoignages,
            'brandings': brandings
        }

    return render(request, 'home_01.html', context)


def test(request):
    brandings = Depositaire.objects.all().values('branding_images').order_by('-date_creation')[:6]
    return HttpResponse(brandings)


