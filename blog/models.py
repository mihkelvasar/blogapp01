from django.db import models
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.TextField(max_length=20, unique=True)
    #While Tag has related_name "posts" as attribute

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField("Post title", max_length=120)
    post_content = models.TextField("Post content")
    post_tags = models.ManyToManyField(to=Tag, related_name="posts", default=None)
    #Post has post_tags attribute
    post_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.post_title}"
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    #pk assignment works

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.TextField("Your name:", max_length=120) 
    author_mail = models.EmailField("Your e-mail:") 
    comment_date = models.DateTimeField(auto_now=True)
    com_content = models.TextField("Your comment:")
    is_active = models.BooleanField()

    