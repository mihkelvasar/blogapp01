from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.forms.models import model_to_dict
from .models import Post
from .forms import *
from . import forms

def index(request): # root/blog
    return HttpResponse(
        "This located at the root folder of blogenv/MyBlog/blog.DO NOT USE FOR PRODUCTION! Just create and register another view."
        )
    #Works

def front(request):
    return render(request, "blog/front.html")

def business(request):
    return HttpResponse("This is the future homepage for aldebaranfoto.ee")

def home(request): #root/blog/home
    return render(request, "blog/home.html")
    #Works

def login_page(request):
    form = forms.LoginForm()
    if request.method =="POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                if user.is_active:
                    request.session.set_expiry(86400)
                    login(request, user)
                    return redirect('blog:front')
            else:
                message = "Did you use the right username and password?"
                return render(request, 'blog/login.html', {'form': form, "message" : message})
    else:
        return render(request, 'blog/login.html', {'form': form})

@login_required   
def logout_request(request):
    logout(request)
    return redirect("blog:archive")

def archive(request): #root/blog/archive
    post_list = Post.objects.filter(post_draft=False).order_by("-created_at")
    tag_list = Tag.objects.all()
    context = {
        "post_list" : post_list,
        "tag_list" : tag_list
        }
    return render(request, "blog/archive.html", context)
    
def adarchive(request):
    post_list = Post.objects.order_by("-updated_at")
    context = {"post_list" : post_list}
    return render(request, 'blog/adarchive.html', context)
    
def postview(request, pk): #root/blog/pk/ - leave for draft management only
    try:
        postone = Post.objects.get(post_id=pk) #I have no idea why, but assigning pk back to post_id works and I get a blank page. 
        comment_count = Comment.objects.filter(post=postone).count()
        tags = postone.post_tags.all()
    except Post.DoesNotExist:
        raise Http404("The post does not exist")
    return render(request, "blog/postsingle.html", {"postone" : postone, "tags" : tags, "comment_count" : comment_count})
    
def commentview (request, pk):
    postone = Post.objects.get(post_id=pk)
    comments = Comment.objects.filter(post=postone).order_by("-comment_date")
    comment_count = Comment.objects.filter(post=postone).count()
    tags = postone.post_tags.all()
    if request.method=="POST":
        new_comment = CommentForm(request.POST)
        if new_comment.is_valid():
            new_comment.instance.is_active = True
            new_comment.instance.post = postone
            new_comment.save()
            return redirect("blog:comments", pk=postone.post_id)
        else:
            message = "All fields are required!"
            new_comment = CommentForm()
            return render(request, "blog/comments.html", {"postone" : postone, "comments" : comments, "message" : message, "new_comment" : new_comment, "comment_count" : comment_count, "tags" : tags})
    else:
        new_comment = CommentForm()
        return render(request, "blog/comments.html", {"postone" : postone, "comments" : comments, "new_comment" : new_comment, "comment_count" : comment_count, "tags" : tags})

def taglist(request, tag_id):
    alltags = Tag.objects.all() #required for listing all available tags
    onetag = get_object_or_404(Tag, tag_id=tag_id)
    taggedposts = Post.objects.filter(post_draft=False, post_tags=onetag).order_by("-created_at") #list of posts with any one tag
    context = {
        "alltags" : alltags,
        "taggedposts" : taggedposts,
        "onetag" : onetag,
    }
    return render(request, "taglist.html", context)
    # create a taglist page that displays posts by tag
    # LvL1 - filter by single tag, selecting another tag changes tag.
    # LvL2 - url with tag_name instead of tag_id
    # LvL3 - filter by multiple tags, perhaps by MMCF
    # see if it works at all

def editview(request, pk): #root/blog/pk/editview 
    post = Post.objects.get(post_id=pk)
    tags = post.post_tags.all()
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.instance.post_id = post.post_id
            form.instance.created_at = post.created_at
            form.save()
            return redirect('blog:postview', pk=post.post_id)
        else:
            form = PostForm(initial=model_to_dict(post))
            return render(request, 'blog/editor.html', {"form" : form, "tags" : tags})
    else:
        form = PostForm(initial=model_to_dict(post))
        return render(request, 'blog/editor.html', {"form" : form, "tags" : tags})

    # PROBLEM: does not post with all tags unselected
    # SOLUTION:

def refuseview(request, pk): #root/pk/refuseview
    postone = Post.objects.get(post_id=pk)
    if request.method=="POST":
        postone.delete()
        return redirect ('blog:archive')
    else:
        return render(request, 'blog/refuse.html', {"postone" : postone})
    
def creatorview(request): #root/creatorview
    if request.method=="POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:postview', pk=form.instance.post_id)
        else:
            form = PostForm()
            return render(request, 'blog/creator.html', {"form" : form})   
    else:
        form = PostForm()
        return render(request, 'blog/creator.html', {"form" : form})
    
    # PROBLEM: if no tags are selected, the form will not POST
    # SOLUTION: 
    
def publish_post(request, pk):
    post = Post.objects.get(post_id=pk)
    if request.method == "POST":
        if post.post_draft == True:
            post.post_draft = False
            post.save()
            return redirect("blog:comments", pk=post.post_id)

def unpublish_post(request, pk):
    post = Post.objects.get(post_id=pk)
    if request.method == "POST":
        if post.post_draft == False:
            post.post_draft = True
            post.save()
            return redirect("blog:postview", pk=post.post_id)
        
def thermos(request, pk): # root/blog/pk/thermos
    rush=Post.objects.get(post_id=pk)
    #return HttpResponse("Folder active for post %s" % rush) # this is necessary to understand how root/blog/directory/subdirectory works
    #this works, but have no idea how or why
    return render(request, 'blog/thermos.html', {"postone" : rush}) #this works as well

def about(request):
    return HttpResponse("This is 'about me' page for the more complex blog")
    # about me, link to github, link to royal road, linkedin
    # build an about me model, this makes it easier to edit, format, as well as export as pdf.

def galleries(request):
    return HttpResponse("This is 'galleries' page for the more complex blog, which shows all galleries")
    # all galleries as a list of titles, photo counts and creation dates

def galleryone(request):
    return HttpResponse("This is 'galleryone' page for the more complex blog, which shows any single gallery")
    # any single gallery, photos on the left, gallery description on the right.
    # gallery object should have a title image.



# SUPERUSER - blogcomp
# PASSWORD - reddit17

