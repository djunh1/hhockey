from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
from django.core.mail import send_mail

from .forms import EmailPostForm

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year)

    return render(request, 'post/detail.html', {'post': post})


def post_share(request, post_id):
    """
    Shares a post with email.
    """
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you check out "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject,
                      message,
                      'info@hopewellhockey.com',
                      [cd['to']],
                      fail_silently=False)
            recipient=cd['to']
            sent = True
    else:
        form = EmailPostForm()
        recipient = False
    return render(request, 'post/share.html', {'post': post, 'form': form, 'sent': sent, 'recipient': recipient} )