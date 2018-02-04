from django.shortcuts import render

def home(request):
    '''
    Render home page
    '''
    welcome = "Welcome to Aashirya's Portfolio"
    context = {'our_greeting':welcome}
    return render(request, 'home.html', context)
