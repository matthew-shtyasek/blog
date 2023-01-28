from django.shortcuts import render, get_object_or_404

from comment.models import Comment
from posts.models import Post


def post_list_view (request):
    posts=Post.objects.filter(published=True)
    context={"post_list": posts,'page':'posts'}
    return render(request, "posts/post_list.html",context)

def post_id_view(request, pk):
    pk = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post = pk, published=True)
    context = {"pk": pk,'page':'posts', 'comments_list':comments}
    return render(request, "posts/post_id.html", context)