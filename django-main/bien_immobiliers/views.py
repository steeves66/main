from django.shortcuts import render

# Create your views here.

from django.db.models import OuterRef, Subquery, Value, F
from django.db.models.functions import Concat
from .models import *
from django.db.models import Prefetch
from django.core.paginator import Paginator



def product_list(request, action):
    # Subquery for depositaire name
    depositaire_subquery = Depositaire.objects.filter(
        id=OuterRef('depositaire_id')
    ).annotate(
        full_name=Concat(F('nom'), Value(' '), F('prenom'))
    ).values('full_name')[:1]
    
    # Subquery for depositaire logo
    depositaire_logo_subquery = Depositaire.objects.filter(
        id=OuterRef('depositaire_id')
    ).values('logo')[:1]
    
    # Subquery for chambre piece_id
    chambre_subquery = BienPiece.objects.filter(
        bien_id=OuterRef('pk'),
        piece_id='chb'
    ).values('piece_id')[:1]
    
    # Subquery for chambre nombre
    chambre_nombre_subquery = BienPiece.objects.filter(
        bien_id=OuterRef('pk'),
        piece_id='chb'
    ).values('nombre')[:1]
    
    filtered_media = Prefetch('bienmedia_set', queryset=BienMedia.objects.filter(media_type__code='img'))

    # Main query  bienmedia_set__bien
    bien_queryset = Bien.objects.prefetch_related(filtered_media).all().annotate(
        depositaire_nom=Subquery(depositaire_subquery),
        depositaire_logo=Subquery(depositaire_logo_subquery),
        chambre=Subquery(chambre_subquery),
        chambre_nombre=Subquery(chambre_nombre_subquery),
    )
    paginator = Paginator(bien_queryset, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    count = bien_queryset.count()
    context = {
        'products': page_obj,
        'count': count
    }
    return render(request, 'biens_immobiliers/properties-list-sidebar.html', context)

def product_details(request, product_id):
    return render(request, 'biens_immobiliers/property-detail-v2.html')