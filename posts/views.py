from django.shortcuts import render

from posts.models import Post


def post_list_view (request):
    posts=Post.objects.filter(published=True)
    context={"post_list": posts}
    return render(request, "posts/post_list.html",context)
# Create your views here.
