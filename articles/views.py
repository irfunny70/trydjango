from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required #decorator
def article_search_view(request):
    query_dict = request.GET# this is a dictionary
    query = query_dict.get("q")#<input type="text",name="q"/>
    article_obj =None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj # used  "object" cos in search.html it is using object
    }
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
def article_create_view(request):
    context = {}  # Define the context dictionary

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        article_object = Article.objects.create(title=title, content=content)
        
        # Now, you can add the created object to the context
        context['object'] = article_object
        context['created'] = True

    return render(request, 'articles/create.html', context=context)