from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            User.objects.create_user(request.POST['username'], password= request.POST['password'])
            return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html',{"error": "Confirmed password isn't write!!!"})
    else:    
        return render(request, 'accounts/signup.html')