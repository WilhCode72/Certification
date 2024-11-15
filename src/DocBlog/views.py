from django.shortcuts import render
from datetime import datetime


def index(request):
    a = datetime.today()
    return render(request, "DocBlog/index.html", context={"date": a})