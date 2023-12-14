from django.contrib import admin

# Register your models here.
from.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title']# this is new to me
    search_fields = ['title','content']

admin.site.register(Article,ArticleAdmin)# check ep 21 on coding entreprenues cos all the things that are need for the blog is done EXCEPT for styling