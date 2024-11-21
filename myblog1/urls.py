# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from myblog1 import views

urlpatterns = [
    path('', views.HOME, name='HomePage'),
    path('PostForm/<int:blog_id>/', views.PostForm, name='PostForm'),
    path('EditPost/<int:post_id>/', views.EditPost, name='EditPost'),
    path('DeletePost/<int:post_id>/', views.DeletePost, name='DeletePost'),
    path('BlogForm', views.BlogForm, name='BlogForm'),
    path('BlogList', views.BlogList, name='BlogList'),
    path('EditBlog/<int:id>/', views.EditBlog, name='EditBlog'),
    path('DeleteBlog/<int:id>/', views.DeleteBlog, name='DeleteBlog'),
    path('BlogDetail/<int:id>/', views.BlogDetail, name='BlogDetail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
