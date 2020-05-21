from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):

    posts = Post.objects.order_by('pub_date')
    return render(request, 'posts/home.html', {'posts': posts})

def post_details(request, post_id):
    return render(request, 'posts/post_detail.html', {'post_id':post_id})

