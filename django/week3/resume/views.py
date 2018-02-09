from django.shortcuts import render
from .models import Experience, Education

# Create your views here.
def experience(request):
#def resume(request):
#    return HttpResponse("Welcome to Resume App")
    qs = Experience.objects.all()
    context = {'Experience' : qs}
    return render(request,'resume/experience.html',context)
def education(request):
#def resume(request):
#    return HttpResponse("Welcome to Resume App")
    qs = Education.objects.all()
    context = {'Education' : qs}
    return render(request,'resume/education.html',context)
