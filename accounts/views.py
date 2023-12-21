from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the admin page upon successful login
        
        context = {"error": "Invalid username or password"}
        return render(request, 'accounts/login.html', context)

    return render(request, 'accounts/login.html', {})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html",{})

def register_view(request):
    return render(request, 'accounts/register.html',{})