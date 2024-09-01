from django.shortcuts import render
from .models import Images_Home

# Create your views here.
def home(request):
    home_images = Images_Home.objects.all()
    
    context = {
        'home_images': home_images
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
