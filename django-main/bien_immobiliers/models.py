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


class Niveau(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Commodite(models.Model):
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
    description = models.TextField(null=True, blank=True)
    
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

    class Meta:
        ordering = ['ordre'] 
    

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
    statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, blank=True, related_name="biens")
    #type_terrain = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_principal = models.ImageField(upload_to='biens/photos', null=True, blank=True)
    plan_principal = models.ImageField(upload_to='biens/plans', null=True, blank=True)
    video_visite = models.ImageField(upload_to='biens/videos', null=True, blank=True)
    standing = models.ForeignKey(Standing, on_delete=models.SET_NULL, null=True, blank=True, related_name="biens")
    date_ajout = models.DateField(auto_now_add=True)
    date_modif = models.DateField(auto_now=True)
    cout_dossier = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    apport_initial = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    type_bien = models.ForeignKey(BienType, on_delete=models.SET_NULL, null=True, blank=True, related_name="biens")
    mode_commercial = models.ForeignKey(ModeCommercial, on_delete=models.SET_NULL, null=True, blank=True, related_name="biens")
    depositaire = models.ForeignKey(Depositaire, on_delete=models.SET_NULL, null=True, related_name="biens")
    pieces = models.ManyToManyField(Piece, through='BienPiece')
    medias = models.ManyToManyField(MediaType, through='BienMedia')
    docs = models.ManyToManyField(Doc, through='BienDoc')
    localisations = models.ManyToManyField(LocalisationType, through='BienLocalisation')
    promotion_immobiliere = models.BooleanField(default=False)         # if bien immobilier
    featured = models.BooleanField(default=False)
    utilisation = models.ForeignKey(Utilisation, on_delete=models.CASCADE, null=True, blank=True, related_name="biens")
    type_maison = models.ForeignKey(TypeMaison, on_delete=models.SET_NULL, null=True, blank=True, related_name="biens")
    nb_piece = models.IntegerField(null=True, blank=True)
    nb_etage = models.IntegerField(null=True, blank=True)             # pour les immeubles
    nb_appartements = models.IntegerField(null=True, blank=True)        # pour les immeubles
    description = models.TextField(null=True, blank=True)
    annee_construction = models.CharField(max_length=50, null=True, blank=True)
    commodites = models.ManyToManyField(Commodite, related_name="biens")
    niveau = models.ManyToManyField(Niveau, through='BienNiveau')

    
    def __str__(self):       
        if self.type_bien.code == "msn":
            return f"{self.type_bien.nom} - {self.type_maison.nom} - {self.nb_piece} pièces "
        return f"{self.type_bien.nom} "
    
    def localisation(self):
        bl = BienLocalisation.objects.filter(bien=self).values_list('valeur', flat=True).order_by('localisation__ordre')
        concatenated_names = " - ".join(bl)
        if concatenated_names.endswith(" - "):
            concatenated_names = concatenated_names[:-1]
        return concatenated_names.title()  


class BienNiveau(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    superficie = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.bien} - {self.niveau.code}"


class BienLocalisation(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    localisation = models.ForeignKey(LocalisationType, on_delete=models.CASCADE)
    valeur = models.CharField(max_length=100)
    

class BienPiece(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    # nombre = models.IntegerField()
    superficie = models.FloatField(null=True, blank=True)
    commodite = models.BooleanField(default=True)                      # si pièce ou espace est  commodité d'une maison si cour arriere - avant - jardin - buanderie - terrain de jeux
    description = models.TextField(null=True, blank=True)
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    niveau = models.ForeignKey(BienNiveau, on_delete=models.CASCADE, null=True, blank=True)

    # class Meta:
    #     unique_together = ('bien', 'piece')
        

class BienMedia(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.SET_NULL, null=True)
    url = models.ImageField(upload_to='medias')
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    niveau = models.ForeignKey(BienNiveau, on_delete=models.CASCADE, null=True, blank=True)
    piece = models.ForeignKey(BienPiece, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # class Meta:
    #     unique_together = ('bien', 'media_type')


class BienDoc(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)

    # class Meta:
    #     unique_together = ('bien', 'doc')
