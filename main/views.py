from django.shortcuts import render


# Create your views here.
def index(request):
    print('main')
    return render(request, 'index.html')

def profile(request):
    print('profile')
    return render(request, 'profile.html')

def projects(request):
    print('projects')
    return render(request, 'projects.html')

def contact(request):
    print('contacts')
    return render(request, 'contact.html')

