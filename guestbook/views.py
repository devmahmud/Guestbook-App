from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm

def index(request):
    posts = Comment.objects.order_by('-date_added')

    context={
        'posts': posts
    }

    return render(request, 'guestbook/index.html', context)

def sign(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment( name=request.POST['name'], comment=request.POST['comment'] )
            new_comment.save()

            return redirect('index')
    
    else:
        form = CommentForm()
            
    context={
        'form': form,
    }

    return render(request, 'guestbook/sign.html', context )