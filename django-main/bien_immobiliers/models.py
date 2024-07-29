from django.db import models

class Piece(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    

class MediaType(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    

class Standing(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    

class ModeCommercial(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
    
class TypeContact(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    

class Depositaire(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='depositaires/logos', null=True, blank=True)
    slogan = models.CharField(max_length=50, null=True, blank=True)
    sous_prefecture = models.CharField(max_length=50, null=True, blank=True)
    commune = models.CharField(max_length=50, null=True, blank=True)
    quartier = models.CharField(max_length=50)
    gps = models.CharField(max_length=20, null=True, blank=True)
    secteur = models.CharField(max_length=50, blank=True, null=True)
    contacts = models.ManyToManyField(TypeContact, through='DepositaireContact')
    personne_morale = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True)
    date_modif = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    

class DepositaireContact(models.Model):
    depositaire = models.ForeignKey(Depositaire, on_delete=models.CASCADE)
    type_contact = models.ForeignKey(TypeContact, on_delete=models.CASCADE)
    valeur = models.CharField(max_length=50, null=True)
    

class BienType(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom

    
class Doc(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    abrege = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
   
   
class Utilisation(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    nom = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nom
    
    
class TypeMaison(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)   
    
    def __str__(self):
        return self.nom
     

class LocalisationType(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=100)
    ordre = models.IntegerField(null=True, blank=True)  
    
    def __str__(self):
        return self.nom
    

class Statut(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)   
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.nom
    


class Bien(models.Model):
    superficie = models.FloatField(null=True, blank=True)
    superficie_habitable = models.FloatField(null=True, blank=True)
    visible = models.BooleanField()
    statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, blank=True)
    #type_terrain = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_principal = models.ImageField(upload_to='biens/photos', null=True, blank=True)
    plan_principal = models.ImageField(upload_to='biens/plans', null=True, blank=True)
    video_visite = models.ImageField(upload_to='biens/videos', null=True, blank=True)
    standing = models.ForeignKey(Standing, on_delete=models.SET_NULL, null=True, blank=True)
    date_ajout = models.DateField(auto_now_add=True)
    date_modif = models.DateField(auto_now=True)
    cout_dossier = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    apport_initial = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type_bien = models.ForeignKey(BienType, on_delete=models.SET_NULL, null=True, blank=True)
    mode_commercial = models.ForeignKey(ModeCommercial, on_delete=models.SET_NULL, null=True, blank=True)
    depositaire = models.ForeignKey(Depositaire, on_delete=models.SET_NULL, null=True)
    pieces = models.ManyToManyField(Piece, through='BienPiece')
    medias = models.ManyToManyField(MediaType, through='BienMedia')
    docs = models.ManyToManyField(Doc, through='BienDoc')
    localisation = models.ManyToManyField(LocalisationType, through='BienLocalisation')
    promotion_immobiliere = models.BooleanField(default=False)         # if bien immobilier
    featured = models.BooleanField(default=False)
    utilisation = models.ForeignKey(Utilisation, on_delete=models.CASCADE, null=True, blank=True)
    type_maison = models.ForeignKey(TypeMaison, on_delete=models.SET_NULL, null=True, blank=True)
    nb_piece = models.IntegerField(null=True, blank=True)
    nb_etage = models.IntegerField(null=True, blank=True)             # pour les immeubles
    nb_appartements = models.IntegerField(null=True, blank=True)      # pour les immeubles
    
    def __str__(self):        
        return self.type_bien.nom
    
    def localisation(self):
        bl = BienLocalisation.objects.filter(bien=self).values_list('valeur', flat=True)
        concatenated_names = " - ".join(bl)
        if concatenated_names.endswith(" - "):
            concatenated_names = concatenated_names[:-1]
        return concatenated_names.title()  


class BienLocalisation(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    localisation = models.ForeignKey(LocalisationType, on_delete=models.CASCADE)
    valeur = models.CharField(max_length=100)
    

class BienPiece(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    nombre = models.IntegerField()

    # class Meta:
    #     unique_together = ('bien', 'piece')
        

class BienMedia(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.SET_NULL, null=True)
    url = models.ImageField(upload_to='medias')
    nom = models.CharField(max_length=50, null=True, blank=True)
    detail = models.BooleanField(default=False, null=True, blank=True)

    # class Meta:
    #     unique_together = ('bien', 'media_type')


class BienDoc(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = ('bien', 'doc')
