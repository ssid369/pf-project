from django.shortcuts import render,get_object_or_404

from .models import intern
def internsh(request):
	interns=intern.objects
	return render(request,'internships/internz.html',{'interns':interns})

def details(request,intern_id):
    internz=get_object_or_404(intern,pk=intern_id)
    return render(request,'internships/details.html',{'intern':internz})


