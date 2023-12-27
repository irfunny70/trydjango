from django import forms 
from.models import Article

# model form
class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains = title)
        if qs.exists():
            raise forms.ValidationError(f'{title} already exists')
        return data

# basic django form
class ArticlesFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    #validation method
    def clean_title(self):#in html code itt is a field error 
        cleaned_data = self.cleaned_data# dictionary
        title = cleaned_data.get('title')
        if title.lower().strip() == "watermelon":
            raise forms.ValidationError("This title is taken")
        return title