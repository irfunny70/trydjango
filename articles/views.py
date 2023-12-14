from django.shortcuts import render
from .models import Article

# Create your views here.

def article_search_view(request):
    context = {}
    return render(request, "articles/search.html", context=context)
    



def article_detail_view(request,id):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request,'articles/details.html',context=context)
#this retun is the one line version of 
# HTML_STRING = render_to_string("home-view.html", context = context)
   # HTML_STRING ="""
    #<h1>{title}</h1>
    #<p>{content}</p>
#""".format(**context)
    #return HttpResponse(HTML_STRING)
