from django.shortcuts import render,HttpResponse,redirect
from .models import BlogPost,Blog
from django.shortcuts import get_object_or_404


# Create your views here.
def HOME(request):
    return render(request, 'Home.html')

def PostForm(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        BlogPost.objects.create(
            title=title,
            description=description,
            blog=blog  
        )
        return redirect('BlogDetail', id=blog.id)

    return render(request, 'PostForm.html', {'blog': blog})

def EditPost(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.description = request.POST.get('description')

       
        post.save()
        return redirect('BlogDetail', id=post.blog.id)
    
    return render(request, 'EditPost.html', {'post': post})

def DeletePost(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    

    blog_id = post.blog.id
    post.delete()
    return redirect('BlogDetail', id=blog_id)


def BlogForm(request):
    if request.method == 'POST':    
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        blogs = Blog(
            title = title,
            description = description,
        )
        blogs.save()
        return redirect('BlogList')

    return render(request, 'BlogForm.html')

def BlogList(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }  
    return render(request, 'BlogList.html',context)

def EditBlog(request, id):
    blog = get_object_or_404(Blog, id=id)
    
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.description = request.POST.get('description')
        blog.save()
        return redirect('BlogList')
        
    return render(request, 'EditBlog.html', {'blog': blog})

def DeleteBlog(request,id):
    Blogs = get_object_or_404(Blog, id=id)
    
    Blogs.delete()
    return redirect('BlogList')

def BlogDetail(request, id):
    blog = get_object_or_404(Blog, id=id)
    posts = blog.posts.all()  
    
    context = {
        'blog': blog,
        'posts': posts
    }

    return render(request, 'BlogDetail.html', context)
        