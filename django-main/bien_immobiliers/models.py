from django.db import models

class Piece(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)
    abrege = models.CharField(max_length=50)

class MediaType(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)

class Standing(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    abrege = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)

class ModeCommercial(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    abrege = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)

class Depositaires(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    logo = models.CharField(max_length=50)
    slogan = models.CharField(max_length=50)
    sous_prefecture = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    secteur = models.CharField(max_length=50)
    emails = models.CharField(max_length=50)
    telephones = models.CharField(max_length=50)
    cellulaires = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    reseaux_sociaux = models.CharField(max_length=50)
    est_personne = models.CharField(max_length=50)
    date_creation = models.DateField()
    date_modif = models.DateField()

class BienType(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    nom = models.CharField(max_length=50)

class Doc(models.Model):
    code = models.CharField(max_length=50, primary_key=True)
    abrege = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)

class Bien(models.Model):
    superficie = models.FloatField()
    superficie_habitable = models.FloatField()
    visible = models.BooleanField()
    statut = models.CharField(max_length=50)
    sous_prefecture = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    secteur = models.CharField(max_length=50)
    type_terrain = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image_principal = models.CharField(max_length=50)
    plan_principal = models.CharField(max_length=50)
    video_visite = models.CharField(max_length=50)
    standing = models.ForeignKey(Standing, on_delete=models.CASCADE)
    date_ajout = models.DateField(auto_now_add=True)
    date_modif = models.DateField(auto_now=True)
    cout_dossier = models.DecimalField(max_digits=10, decimal_places=2)
    apport_initial = models.DecimalField(max_digits=10, decimal_places=2)
    type_bien = models.ForeignKey(BienType, on_delete=models.CASCADE)
    mode_commercial = models.ForeignKey(ModeCommercial, on_delete=models.CASCADE)
    depositaire = models.ForeignKey(Depositaires, on_delete=models.CASCADE)
    pieces = models.ManyToManyField(Piece, through='BienPiece')
    medias = models.ManyToManyField(MediaType, through='BienMedia')
    docs = models.ManyToManyField(Doc, through='BienDoc')

class BienPiece(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    class Meta:
        unique_together = ('bien', 'piece')

class BienMedia(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    url = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)

    class Meta:
        unique_together = ('bien', 'media_type')

class BienDoc(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    doc = models.ForeignKey(Doc, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('bien', 'doc')
