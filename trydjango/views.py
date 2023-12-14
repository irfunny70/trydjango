from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string


def home_view(request,*args, **kwargs):
    article_obj = Article.objects.get(id = 1)
    article_queryset = Article.objects.all()
    
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    #django template for now we use this
    HTML_STRING = render_to_string("home-view.html", context = context)
   # HTML_STRING ="""
    #<h1>{title}</h1>
    #<p>{content}</p>
#""".format(**context)
    return HttpResponse(HTML_STRING)