from django.shortcuts import render

# Create your views here.
def login_render(request):
    return render(request, "authapp/login.html")

def company_registration(request):
    return render(request, "authapp/companyRegister.html")

def enterCompanyID(request):
    return render(request, "authapp/enterCompanyID.html")