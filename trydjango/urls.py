"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home_view
from articles.views import (
    article_create_view,
    article_detail_view,
    article_search_view,
)
from accounts.views import (
    login_view,
    logout_view,
    register_view,
)
urlpatterns = [
    path('',home_view),#trydjango views
    path('articles/',article_search_view),#article views
    path('articles/create/',article_create_view),#article views
    path('articles/<int:id>',article_detail_view),#<int:id> make the url more dynamic when user click on in so it can be articles/1/ or article/2/
    path('admin/', admin.site.urls),#django 
    path('login/',login_view),# accounts views
]
