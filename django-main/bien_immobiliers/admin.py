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
        ('biens', {'fields': ('type_bien', ('type_maison', 'nb_piece', 'utilisation',), ('superficie', 'superficie_habitable',), 'standing',)}),
        ('Bien immobiliers', {'fields': ('promotion_immobiliere', ('apport_initial', 'cout_dossier'),)}),
        ('Coût', {'fields': (('mode_commercial', 'prix'), )}),
        ('Images', {'fields': ('image_principal', 'plan_principal', 'video_visite'),}),
        ('autres', {'fields': ('featured', 'visible', 'statut',)}),
        )
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))
        return "No Image"

    image_tag.short_description = 'Image'
    
admin.site.register(Bien, BienAdmin)

















