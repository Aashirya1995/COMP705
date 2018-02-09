from django.shortcuts import render

def home(request):
    '''
    Render home page
    '''
    welcome = "Welcome to Aashirya's Portfolio"
    context = {'our_greeting':welcome}
    return render(request, 'home.html', context)

def resume(request):
    '''
    Renders the Resume
    '''
    resume_one = "Resume"
    context = {'my_resume':resume_one}
    return render(request, 'resume.html', context)

def portfolio(request):
    '''
    Renders the Portfolio
    '''
    portfolio_one = "Portfolio"
    context = {'my_portfolio' : portfolio_one}
    return render(request, 'portfolio.html', context)

def contact(request):
    '''
    Renders the contact form template
    '''
    contact_one = "Contact"
    context = {'my_contact': contact_one}
    return render(request, 'contact.html', context)
