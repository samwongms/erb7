from django.shortcuts import render
from listings.models import Listing
from django.http import HttpResponse



# Create your views here.
def index(request):
    listings = Listing.objects.filter(is_published=True)[:3]
    context = {'listings': listings}
    return render(request, 'pages/index.html', context)

#def index(request):
    #return HttpResponse("<h1>Hello, World!</h1>")

def about(request):
    return render(request,'pages/about.html')

