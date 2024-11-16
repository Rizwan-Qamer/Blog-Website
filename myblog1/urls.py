from django.urls import path
from myblog1 import views

urlpatterns = [
    path('', views.HOME, name='HomePage'),
    path('PostForm/<int:blog_id>/', views.PostForm, name='PostForm'),  # Updated to accept blog_id
    path('EditPost/<int:post_id>/', views.EditPost, name='EditPost'),
    path('DeletePost/<int:post_id>/', views.DeletePost, name='DeletePost'),
    path('BlogForm', views.BlogForm, name='BlogForm'),
    path('BlogList', views.BlogList, name='BlogList'),
    path('EditBlog/<int:id>/', views.EditBlog, name='EditBlog'),
    path('DeleteBlog/<int:id>/', views.DeleteBlog, name='DeleteBlog'),
    path('BlogDetail/<int:id>/', views.BlogDetail, name='BlogDetail'),
]   