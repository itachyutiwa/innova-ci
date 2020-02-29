from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title':'BIENVENUE'
    }
    return render(request, 'index.html', context)

def inscription(request):
    context={
        'title':'INSCRITION'
    }
    return render(request, 'reservation.html', context)