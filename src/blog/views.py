from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def article(request, numero_article):
    return render(request, f"blog/article-{numero_article}.html")

