from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import ArticlesForm

# Create your views here.
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

@login_required #decorator
def article_create_view(request):
    form = ArticlesForm(request.POST or None)  # passing unclean data to this form class/handle data
    context = {
        "form": form
    }  #render the form

    if form.is_valid():#this chonk of if statement is to make sure the data is being clean
            article_object = form.save()#model form one line 
            context['form'] = ArticlesForm
            # down here is the basic form
            # title = form.cleaned_data.get("title")
            # content = form.cleaned_data.get("content")
            # article_object = Article.objects.create(title=title, content=content)      
            # Now, you can add the created object to the context
            context['object'] = article_object
            context['created'] = True
        
    return render(request, 'articles/create.html', context=context)