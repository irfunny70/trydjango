from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data =request.POST)
        if form.is_valid():# only work with authentication form
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to the home page upon successful login      
    else:
        form = AuthenticationForm(request)
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html",{})

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")
    context = {"form": form}
    return render(request, 'accounts/register.html',context)