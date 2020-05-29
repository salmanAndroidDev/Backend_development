from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:            
            post = Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author =  request.user

            post.save()
            return redirect('home')

        else:
            return render(request, 'create.html',{'error': 'Please fill both fields!'})

    else:
        return render(request, 'create.html')

def home(request):    
    posts = Post.objects.order_by('votes_total')        
    return render(request, 'home.html', {'posts': posts})

def upvote(request, pk):
    post = Post.objects.get(pk= pk)
    post.votes_total += 1
    post.save()    
    return redirect('home')

def downvote(request, pk):
    post = Post.objects.get(pk= pk)
    if post.votes_total > 0:
        post.votes_total -= 1
        post.save()
    return redirect('home')


