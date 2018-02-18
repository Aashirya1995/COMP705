from django.shortcuts import render
from .models import Experience, Education,Resume

# Create your views here.
def resume(request):
    '''
    Renders Resume
    '''
#def resume(request):
#    return HttpResponse("Welcome to Resume App")
    my_resume = Resume.objects.first()
    #exp_qs = Resume.get_experience()
    context = {'my_resume' : my_resume}
    return render(request,'resume/resume.html',context)
