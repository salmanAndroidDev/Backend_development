from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def show_and_error(request, page_name, msg):
    return render(request, 'accounts/{}'.format(page_name), {"error": msg})


# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username= request.POST['username'])
                return show_and_error(request, 'signup.html', "This User already exists!!!")
            except User.DoesNotExist  as e:
                user = User.objects.create_user(request.POST['username'], password= request.POST['password'])
                login(request, user)
                return redirect('home')
        else:
            return show_and_error(request, 'signup.html', "Confirmed password isn't write!!!")
    else:    
        return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        
        user = authenticate(username= request.POST['username'], password = request.POST["password"])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        else:
            return show_and_error(request, 'login.html', 'These info is not authentic!')

    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    else:
        return redirect('home')