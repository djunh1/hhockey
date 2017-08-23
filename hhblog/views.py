from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag

from .forms import EmailPostForm, CommentForm

def post_list(request, tag_slug=None):
    """
    Returns posts lists.  Uses Tags to filter posts.
    """
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/list.html', {'page': page,
                                                   'posts': posts,
                                                   'tag': tag})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year)
    comments = post.comments.filter(active=True)
    new_comment_add = False
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            new_comment_add = True
    else:
        comment_form = CommentForm()

    return render(request, 'post/detail.html', {'post': post,
                                                'comments': comments,
                                                'comment_form': comment_form,
                                                'new_comment_add': new_comment_add})


def post_share(request, post_id):
    """
    Shares a post via email.
    """
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = 'HOPEWELL HOCKEY user - {} ({}) recommends you check out "{}"'.format(cd['name'], cd['email'],
                                                                                     post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject,
                      message,
                      'info@hopewellhockey.com',
                      [cd['to']],
                      fail_silently=False)

            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'post/share.html', {'post': post, 'form': form, 'sent': sent})