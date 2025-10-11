from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.http import urlencode

# Create your views here.

def blog_view(request, **kwargs):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(),
        status=1
    ).order_by('-published_date')

    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    last_post = posts.first()
    last_author = last_post.author if last_post else None

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        posts = paginator.get_page(1)

    context = {
        'posts': posts,
        'author': last_author,
    }
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(
        Post,
        id=pid,
        status=1,
        published_date__lte=timezone.now()
    )

    post.counted_views += 1
    post.save(update_fields=['counted_views'])

    posts_list = list(Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date'))
    current_index = posts_list.index(post)
    prev_post = posts_list[current_index - 1] if current_index > 0 else None
    next_post = posts_list[current_index + 1] if current_index < len(posts_list) - 1 else None

    if post.login_require and not request.user.is_authenticated:
        login_url = reverse('accounts:login')
        query_string = urlencode({'next': request.get_full_path()})
        url = f"{login_url}?{query_string}"
        return HttpResponseRedirect(url)

    comments = Comment.objects.filter(post=post, approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if not comment.subject:
                comment.subject = None
            comment.save()
            messages.success(request, 'Your comment submitted successfully!')
        else:
            messages.error(request, 'Your comment did not submit!')
    else:
        form = CommentForm()

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'comments': comments,
        'form': form,
        'author': post.author,  # نویسنده همان پست
    }
    return render(request, 'blog/blog-single.html', context)