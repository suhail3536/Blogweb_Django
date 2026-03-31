from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def home(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/home.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  
    return render(request, 'blogapp/post_detail.html', {'post': post})



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')   # home pe bhej dega
    else:
        form = PostForm()

    return render(request, 'blogapp/create_post.html', {'form': form})

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm(instance=post)

    return render(request, 'blogapp/edit_post.html', {'form': form})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('/')

    return render(request, 'blogapp/delete_confirm.html', {'post': post})
