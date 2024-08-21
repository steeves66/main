from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from django.db.models import OuterRef, Subquery, Value, F
from django.db.models.functions import Concat
from .models import *
from django.db.models import Prefetch
from django.core.paginator import Paginator


def test(request):
    return HttpResponse('test')


def product_details(request, product_id):
    product = get_object_or_404(Bien, id=product_id, visible=True)
    pieces_int = BienPiece.objects.filter(bien=product, commodite=True)
    pieces_ext = BienPiece.objects.filter(bien=product, commodite=False)
    localisation = BienLocalisation.objects.filter(bien=product).order_by('localisation__ordre')

    plans = BienMedia.objects.filter(bien=product, media_type="pln", niveau__isnull=False)

    images = BienMedia.objects.filter(bien=product, media_type="img")
    docs = product.docs

    context = {
        "product": product,
        "pieces_int": pieces_int,
        "pieces_ext": pieces_ext,
        "localisation": localisation,
        "plans": plans,
        "images": images,
        "docs": docs,
    }
    
    return render(request, 'biens_immobiliers/property-detail-v2.html', context)


def product_list(request, type, filter):
    match type:
        case 'vente':
            product = Bien.objects.filter(mode_commercial='vnt', visible=True).order_by('-date_ajout')

        case 'location':
            product = Bien.objects.filter(mode_commercial='loc', visible=True).order_by('-date_ajout')

        case 'featured':
            product = Bien.objects.filter(visible=True, featured=True)

        case 'bien_immobilier':
            product = Bien.objects.filter(promotion_immobiliere=True, visible=True).order_by('-date_ajout')

        case 'mode_commercial':
            product = Bien.objects.filter(mode_commercial__code__exact=filter, visible=True).order_by('-date_ajout')

        case 'ville':
            product = Bien.objects.filter(bienlocalisation__localisation='vle', bienlocalisation__valeur__icontains=filter, visible=True).order_by('-date_ajout')

        case 'type_maison':
            product = Bien.objects.filter(type_maison__code__exact=filter, visible=True).order_by('-date_ajout')

        case 'type_bien':
            product = Bien.objects.filter(type_bien__code__exact=filter, visible=True).order_by('-date_ajout')

        case 'none':
            product = Bien.objects.filter(visible=True).order_by('-date_ajout')

    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    count = product.count()
    context = {
        'products': page_obj,
        'count': count
    }
    return render(request, 'biens_immobiliers/properties-list-sidebar.html', context)

