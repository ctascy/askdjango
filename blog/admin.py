from django.contrib import admin
from blog.models import Post, Comment, Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'get_tag_names']
    #매니투매니는..
    def get_tag_names(self, post):
        return ','.join([tag.name for tag in post.tags.all()])

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
