from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Register your models here.

# admin.site.register(Bien)


admin.site.register(Piece)


class BienPieceInline(admin.TabularInline):
    model = BienPiece
    extra = 2
    
    
class BienMediaInline(admin.TabularInline):
    model = BienMedia
    extra = 2


class BienDocInline(admin.TabularInline):
    model = BienDoc
    extra = 2
    

class DepositaireContactInline(admin.TabularInline):
    model = DepositaireContact
    extra = 3
    

class BienLocalisationInline(admin.TabularInline):
    model = BienLocalisation
    extra = 3


class DepositaireAdmin(admin.ModelAdmin):
    inlines = (DepositaireContactInline, )
    fieldsets = (
        ('Dépositaires', {'fields': ('personne_morale', ('nom', 'prenom',), ('logo', 'slogan',), )}),
        ('Localisation', {'fields': (('sous_prefecture', 'commune'), ('quartier', 'secteur'), 'gps',)}),
        )
    
admin.site.register(Depositaire, DepositaireAdmin)

class BienAdmin(admin.ModelAdmin):
    inlines = (BienPieceInline, BienMediaInline, BienLocalisationInline, BienDocInline, )
    fieldsets = (
        ('Dépositaires', {'fields': ('depositaire',)}),
        ('biens', {'fields': ('type_bien', 'type_maison', 'nb_piece', 'utilisation', 'superficie', 'superficie_habitable', 'standing',)}),
        ('Coût', {'fields': ('mode_commercial', 'prix', )}),
        ('Bien immobiliers', {'fields': ('promotion_immobiliere', 'apport_initial', 'cout_dossier',)}),
        ('Immeuble', {'fields': ('nb_etage', 'nb_appartements',)}),
        ('Statuts', {'fields': ('featured', 'visible', 'statut',)}),
        ('Images', {'fields': ('image_principal', 'plan_principal', 'video_visite',)}),
        )
    
    def image_tag(self, obj):
        if obj.image_principal:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image_principal.url))
        return "No Image"
    
    def plan_tag(self, obj):
        if obj.plan_principal:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.plan_principal.url))
        return "No Plan"

    image_tag.short_description = 'Image'
    plan_tag.short_description = 'Plan'
    list_display = ['biens', 'image_tag', 'plan_tag']
    
    
    def biens(self, obj):
        bl = BienLocalisation.objects.filter(bien=obj).values_list('valeur', flat=True)
        concatenated_names = " - ".join(bl)
        if concatenated_names.endswith(" - "):
            concatenated_names = concatenated_names[:-1]
        
        if obj.type_bien.nom == 'terrain':
            return f"{obj.type_bien.nom}    :    {obj.prix} F    : {obj.superficie} m2 : {concatenated_names}"
        else:
            return f"{obj.type_bien.nom}    : {obj.nb_piece} pièces    :{obj.prix} F    :   {obj.superficie} m2 : {concatenated_names}"
    
admin.site.register(Bien, BienAdmin)

















