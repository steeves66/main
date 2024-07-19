from django.shortcuts import render

# Create your views here.

def product_list(request, action):
    return render(request, 'biens_immobiiers/properties-list-sidebar.html')

def product_details(request, id):
    return render(request, 'biens_immobiiers/property-detail.html')