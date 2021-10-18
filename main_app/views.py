from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Post
# Real python
from main_app.forms import CustomUserCreationForm
from django.urls import reverse # real python
from django.contrib.auth import login

# Create your views here.
def index(request):
    # return HttpResponse("It works")
    return render(request, 'base.html')

def home(request):
    response = "Todos los Posts" 
    #tl = Post.objects.order_by('-time')[:5]
    tl = Post.objects.all().order_by('-time')
    #template = loader.get_template('home/tl.html')
    context = { 'tl': tl }
    # return HttpResponse(template.render(context, request))
    return render(request, 'home/tl.html', context)

def detail(request, post_id):
    contenido = Post.objects.get(id=post_id)
    context = { 'contenido' : contenido }
    print (contenido.user.name)
    print (context['contenido'])
    # return HttpResponse('Post id = %i.' % post_id)
    return render(request, 'post/detail.html', context)

def userpage(request, user_id):
    # Render all posts by user DOESN'T WORK
    # TODO: Fix this!!
    contenido = Posts.objects.filter(user=user_id)
    print(user)
    context = { 'contenido' : contenido }
    return render(request, 'user/home.html', context)

def register(request):
    if request.method == "GET":
        return render(
            request, "registration/register.html",
            { "form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print("####")
        print(form.errors ) ####
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse("home"))
    # return HttpResponse('Houston, tenemos un problema!!')