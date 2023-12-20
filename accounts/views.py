from django.shortcuts import render
from django.contrib.auth import login, authenticate 

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username)
        password = authenticate(request, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, 'accounts/login.html',context)
    return render(request, 'accounts/login.html',{})

def logout_view(request):
    return render(request, "accounts/logout.html",{})

def register_view(request):
    return render(request, 'accounts/register.html',{})