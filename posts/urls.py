from django.urls import path

from posts.views import post_list_view, post_id_view

app_name="posts"
urlpatterns=[
    path("",post_list_view),
    path("post/<int:pk>", post_id_view, name="post"),
]
