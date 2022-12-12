from django.shortcuts import render

# Create your views here.

def m_Home(request):
    return render(request, 'mobile/m-home.html')

def M_Jm_Submit(request):
    return render(request, 'mobile/m-jm-submit.html')