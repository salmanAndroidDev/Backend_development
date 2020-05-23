from django.shortcuts import render
from .models import Admin_info
# Create your views here.
def about(request):
    info = Admin_info.objects.all()[0]
    return render(request, 'about/about.html',{'info': info})