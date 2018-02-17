from django.shortcuts import render
from .models import Experience, Education

# Create your views here.
def resume(request):
#def resume(request):
#    return HttpResponse("Welcome to Resume App")
    qs = Experience.objects.all()
    eduqs = Education.objects.all()
    context = {'Experience' : qs, 'Education' : eduqs}
    return render(request,'resume/resume.html',context)
