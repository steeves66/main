

def get_property_detail(id):
    pass


def get_properties_vedette():
   return Bien.objects.filter(featured=True,visible=True).order_by('-date_ajout')[:4]


def get_properties_by_type(type):
    pass


def get_properties_by_mode(mode):
    pass


def get_properties_by_city(city):
    pass


def get_immo_properties():
    # biens immobiliers
    pass


def get_immo_properties_by_mode(mode):
    pass


def get_immo_properties_by_standing(standing):
    # limit by 7
    pass


def get_testimoies_list():
    pass


def get_depositaires_logo():
    pass



""" Home page """"

searchProduct by mode commercial

searchProduct by type de maison

searchProduct by vedette

searchProduct terrain by mode commerciale

searchProduct terrain

searchProduct maison immobiliere by mode commerciale

searchProduct maison immobiliere


"""  detail page """

searchProduct by id


"""  search engine """

