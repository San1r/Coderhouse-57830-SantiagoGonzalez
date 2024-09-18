from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Avatar, Image
from .forms import Posting, CommentForm, PostSearchForm, ImageForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied

def home(request):
    form = PostSearchForm(request.GET or None)
    posts = Post.objects.all().order_by('-published_date')

    avatar = None
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=request.user)
        except Avatar.DoesNotExist:
            avatar = None

    if form.is_valid():
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        username = form.cleaned_data.get('username')

        if start_date:
            posts = posts.filter(published_date__gte=start_date)
        if end_date:
            posts = posts.filter(published_date__lte=end_date)
        if username:
            posts = posts.filter(author__username__icontains=username)

    return render(request, "blog/home.html", {
        'posts': posts,
        'form': form,
        'avatar': avatar,
    })

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(approved=True).order_by('-created_date')

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = Comment(
                    post=post,
                    user=request.user,
                    content=comment_form.cleaned_data['content'],
                    created_date=timezone.now()
                )
                new_comment.save()
                return redirect('post', post_id=post.id)
        else:
            return redirect('login')

    else:
        comment_form = CommentForm() if request.user.is_authenticated else None

    return render(request, "blog/post.html", {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def posting(request):
    if request.method == 'POST':
        posting_form = Posting(request.POST, request.FILES)
        if posting_form.is_valid():
            new_post = posting_form.save(commit=False)
            new_post.published_date = timezone.now()
            new_post.author = request.user
            new_post.save()

            if 'image' in request.FILES:
                image = request.FILES['image']
                new_image = Image(
                    post=new_post,
                    image=image
                )
                new_image.save()

            return redirect('home')

    else:
        posting_form = Posting()

    return render(request, "blog/posting.html", {
        "posting": posting_form
    })

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if post.author != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = Posting(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post', post_id=post.id)
    else:
        form = Posting(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('home')

@login_required
def upload_image(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            new_image = image_form.save(commit=False)
            new_image.post = post
            new_image.save()
            return redirect('post', post_id=post.id)
    else:
        image_form = ImageForm()

    return render(request, 'blog/upload_image.html', {'form': image_form, 'post': post})

def about(request):
    return render(request, 'blog/about.html')
