"""Views for app posts.
"""
from django.shortcuts import render, get_object_or_404


from .models import Post, Group

POST_LIMIT = 10


# Main page
def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте.'
    posts = Post.objects.all()[:POST_LIMIT]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


# Guests page
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = f'Записи сообщества {get_object_or_404(Group, slug=slug)}'
    group = get_object_or_404(Group, slug=slug)
    # posts = Post.objects.filter(group=group)[:POST_LIMIT]
    posts = group.posts.all()
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
