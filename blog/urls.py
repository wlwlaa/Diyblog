from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.PostListView.as_view(), name='blogs'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('bloggers/', views.AuthorListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('<int:pk>/create', views.CommentCreate.as_view(), name='comment'),
    path('create/', views.PostCreate.as_view(), name='post-create'),
]