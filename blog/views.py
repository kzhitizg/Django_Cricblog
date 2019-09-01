from django.shortcuts import render, redirect
from .models import Blog
from django.db.models import Count
from .form import Blog_form
# Create your views here.

def home_page(req, *args, **kwargs):
    context= {
        "blogs": Blog.objects.all()
    }
    return render(req, "index.html", context)

def new_blog(req, *args, **kwargs):
    form= Blog_form(req.POST or None)
    if form.is_valid():
        form.save()
        form= Blog_form()
        return redirect('/')

    context={
        "form": form
    }
    return render(req, "new.html", context)

def show_blog(req, *args, **kwargs):
    context={'blog':Blog.objects.get(id=kwargs['id'])}
    return render(req, "show.html", context)

def delete_view(req, *args, **kwargs):
    Blog.objects.filter(id=kwargs['id']).delete()
    return redirect('/')