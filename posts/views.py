from django.shortcuts import render, get_object_or_404

from comment.forms import CommentForm
from comment.models import Comment
from posts.models import Post


def post_list_view (request):
    posts=Post.objects.filter(published=True)
    context={"post_list": posts,'page':'posts'}
    return render(request, "posts/post_list.html",context)

def post_id_view(request, pk):
    pk = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post = pk, published=True)
    if request.method=="GET": #если метод запроса GET
        form = CommentForm(request.GET) #то мы передаём запрос в форму
        if form.is_valid(): #если форма заполнена корректно
            comment =  form.save(commit=False) #получаем объект комментария без сохранения
            comment.post = pk #записываем к какому посту относится данный комментарий
            comment.save() #комментарий сохраняется
            form = CommentForm() #создаём новую форму

    context = {"pk": pk,'page':'posts', 'comments_list':comments, 'form':form}
    return render(request, "posts/post_id.html", context)