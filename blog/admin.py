from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    fieldsets = [
        ("Title", {"fields" : ["post_title"]}),
        ("Post contents", {"fields" : ["post_content"]}),
        ("Originally posted", {"fields" : ["created_at"]}),
        ("Last updated", {"fields" : ["updated_at"]})
    ]
    
    list_display = ["post_title", "created_at", "updated_at"]
    list_filter = ["created_at", "updated_at"]

admin.site.register(Post, PostAdmin)

# Register your models here.

#"auto_now" and "auto_now_add" can be used in models, for updated_at and created_at but in admin.py they CANNOT be displayed as editable fields, 
# solution - read_onlyfields - now posts can be edited from both admin as well as web page 10.45

# successful edit now redirects to postsingle.html (post detail view), unsuccessful edit reloads editor.html (post edit view)

#replaced "reset" button in editview with "Back" button 11.10

#replaced "edit" and "delete" links in "post detailed view" with buttons

#created refuse.html for deleteview. added buttons "Delete" (does nothing right now) and "Back" (goes back to to "post detailed view") 11.28

#delete view works 00.45

#replacing links <a href="/location"></a> with buttons now works (althouhg inline buttons only work within forms).
# Was that god damn leading '/' that kept ruining things this also fixed redirects and reloads after a redirect.

# fixed that only the affirmative choice invokes request.method=="POST" and thus editview or deleteview, negative choice button has to remain outside
#the form. 02.11

#reloading the post-deletion main archive landing page still causes error

#created view for adding posts. used forms.py and form class 04.38