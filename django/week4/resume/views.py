from django.shortcuts import render
from .models import Experience, Education,Resume

# Create your views here.
def resume(request):
#def resume(request):
#    return HttpResponse("Welcome to Resume App")
    qs = Resume.objects.first()
    #exp_qs = Resume.get_experience()
    context = {'Resume' : qs}
    return render(request,'resume/resume.html',context)
