from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Post
from .forms import *

def index(request): # root/blog
    return HttpResponse(
        "This located at the root folder of blogenv/MyBlog/blog.DO NOT USE FOR PRODUCTION! Just create and register another view."
        )

def home(request): #root/blog/home
    post_list = Post.objects.order_by("-updated_at")[:5] #shows the last 5 posts
    context = {"post_list" : post_list}
    return render(request, "blog/home.html", context)

def archive(request): #root/blog/archive
    post_list = Post.objects.order_by("-updated_at")
    context = {"post_list" : post_list}
    return render(request, "blog/archive.html", context)

def postview(request, pk): #root/blog/pk/
    try:
        postone = Post.objects.get(post_id=pk) #I have no idea why, but assigning pk back to post_id works and I get a blank page. 
    except Post.DoesNotExist:
        raise Http404("The post does not exist")
    return render(request, "blog/postsingle.html", {"postone" : postone})

def editview(request, pk): #root/blog/pk/editview 
    yellow = Post.objects.get(post_id=pk)
    if request.method=="POST":
        new_title = request.POST['ptitle']
        new_content = request.POST['pcontent'] 
        
        yellow.post_title = new_title
        yellow.post_content = new_content
        yellow.save()
        return render(request, 'blog/postsingle.html', {"postone" : yellow})
    else:
        return render(request, 'blog/editor.html', {"postone" : yellow})

def refuseview(request, pk): #root/pk/refuseview
    postone = Post.objects.get(post_id=pk)
    post_list = Post.objects.order_by("-updated_at")
    if request.method=="POST":
        postone.delete()
        return render(request, 'blog/archive.html', {"post_list" : post_list})
    else:
        return render(request, 'blog/refuse.html', {"postone" : postone})
    
def creatorview(request): #root/creatorview
    if request.method=="POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'blog/postsingle.html', {"postone" : post})    
    else:
        form = PostForm()
        return render(request, 'blog/creator.html', {"form" : form})

def thermos(request, pk): # root/blog/pk/thermos
    rush=Post.objects.get(post_id=pk)
    #return HttpResponse("Folder active for post %s" % rush) # this is necessary to understand how root/blog/directory/subdirectory works
    #this works, but have no idea how or why
    return render(request, 'blog/thermos.html', {"postone" : rush}) #this works as well

# Create your views here.
