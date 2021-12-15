from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from .models import Comment, Post
from django.http import HttpResponseRedirect
from django.contrib.messages import get_messages
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect
import datetime,os
time = datetime.datetime.now()
time = time.strftime("%H:%M:%S")
User = get_user_model()
# Create your views here.

def allow(answer, use, request):
   user = User.objects.all()
   post = Post.objects.all()
   comment = Comment.objects.all()
   if answer == "render" and use is not None:
      return render(request, "home.html", {"login":True, "user":use, "post":post, "comment":comment, "users":user})
   if answer == "render" and use is None:
      return render(request, "home.html", {"login":False})
   if answer == "redirect" and use is None:
      return redirect('/', {"login":False})

def home(request):
   me = request.session.get('me', 'mee')
   user = User.objects.filter(username=me).exists()
   if User.objects.filter(username=me).exists():
      user = User.objects.get(username=me)
      return allow("render", user, request)
   else:
      return render(request, "home.html", {"login":False})

def edit_post(request, id):
   if request.method == "POST":
     id = int(id)
     con = request.POST["content"]
     title = request.POST["title"]
     post = Post.object.get(id=id)
     post.set_content(con)  
     post.set_title(title)
     post.save() 
     return redirect('/')
   else:
      return HttpResponse('actually its not us but you the link you followed is broken 🚀🚀🚀')

def password(request):
   if request.method == "POST":
      me = request.session.get('me', 'mee')
      if User.objects.filter(username=me).exists():
         password1     = request.POST["password1"]
         password2     = request.POST["password2"]
         user = User.objects.get(username=me)
         passwod = user.password
         if password1 == password2:
           if password1 == passwod:
             messages.info(request, ':) the password is not differnt from the current one')
             return redirect('/')
           else:
             user.password=password1
             user.save()
             messages.info(request, 'from '+str(passwod)+' to'+str(password1)+' sucessfully')
             return redirect('/')
         else:
           messages.info(request, ':) the password do not match')
           return redirect('/')
      else:
         return HttpResponse('log in first 🚀🚀🚀')
   else:
      return redirect('/')
      
def update_profile(request, username):
   if request.method == "POST":
      username           = request.session.get("me")
      email             = request.POST["email"]
      rank             = request.POST["rank"]
      verified            = request.POST["verified"]
      username          = request.POST["username"]
      about             = request.POST["about"]
      location          = request.POST["location"]
      user              = User.object.get(username=username)
      user.email        = email
      user.rank        = rank
      user.verified       = verified
      user.username     = username
      user.about        = about
      user.location     = location
      user.save()
      messages.info(request, ':) '+str(username)+', your profile update successfully')
      return redirect('/')
   else:
      return redirect('/')

def user(request, username):
   user = User.objects.filter(username=username).exists()
   if User.objects.filter(username=username).exists():
      user = User.objects.get(username=username)
      if  request.session['me'] == user.username:
         print(request.session['me'])
         return render (request, "profile.html", {"user":user, "login":True})
      else:
         return render (request, "profile.html", {"user":user,"login":False})
   else:
      return HttpResponse('actually its not us but you the link you followed is broken 🚀🚀🚀')

def comment(request):
   if request.method == "POST":
      idd = request.POST["idd"]
      comment = request.POST["comment"]
      #posterimg = request.POST["posterimg"]
      comment = Comment.objects.create(idd=idd, comment=comment, posterimg=None, time=time)
      comment.save()
      return  redirect('/')
   else:
      return  redirect('/')

def post(request):
   if request.method == "POST":
    image = request.POST.get("image")
    if image is not None:
      content = request.POST["content"]
      image = request.POST.get("image")
      title = request.POST["title"]
      posterimage = request.POST["posterimage"]
      post = Post.objects.create(image=image, content=content, title=title, posterimage=posterimage, time=time)
      post.save()  
      post = Post.objeccts.get(image=image)
      initial_path = post.image.path
      post.image.name = post.id
      new_path = settings.MEDIA_ROOT + post.image.name
      os.rename(initial_path, new_path)
      post.save()
      return  redirect('/')
    elif image is None:  
      content = request.POST["content"]
      title = request.POST["title"]
      posterimage = request.POST["posterimage"]
      post = Post.objects.create(content=content, title=title, posterimage=posterimage, time=time, image=None)
      post.save()  
      return  redirect('/')
   else:
      return  redirect('/')

def hoome(request):
   num_visit = request.session.get('num_visit', 1)
   if num_visit is not None:
      num_visit = num_visit + 1
      request.session['num_visit'] = num_visit
      if num_visit >=2:
         request.session['num_visit'] = 0
      return HttpResponse('view count ' + str(num_visit))
   if num_visit is None:
     num_visit = request.session.get('num_visit', 0) + 2
     request.session['num_visit'] = num_visit
     return HttpResponse('view count ' + str(num_visit)) 

def logout(request):
   out = request.session.get('me')
   out = "logout"
   request.session['me'] = out
   message = "log out Successfully, but why?"
   #return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {"msg":message})
   #return request.META.get('HTTP_REFERER', {"msg":message})
   return redirect('/', {"msg":message})

@csrf_exempt
def login(request):
   if request.method =="POST":
     password = request.POST['password']
     username = request.POST['username']    
     if User.objects.filter(username=username, password=password).exists():
        out = username
        request.session['me'] = out
        return redirect('/')
     else:
        message = 'Wrong Username Or Password'
        return render (request,'login.html', {"msg":message})
   else:
      return render(request, 'login.html')

@csrf_exempt
def signup(request):
   if request.method == "POST":
      fname    = "your first_name"
      lname    = "your last_name"
      about    = "about you here!"
      email    = request.POST["email"]
      username = request.POST["username"]
      psswd1   = request.POST["password1"]
      psswd2   = request.POST["password2"]
      if psswd1 == psswd2:
         if User.objects.filter(username=username).exists():
            message = 'Username Taken! :)'
            return redirect('/signup', {"msg":message})
         elif User.objects.filter(email=email).exists():
            message = "Someone Is Using That Email"
            return  reverse('Signup', {"msg":message})
         else:
            user = User.objects.create_user(first_name=fname, about=about, image=None, location=None, rank=None, last_name=lname, username=username, password=psswd1, email=email)
            user.save()
            me = user.username
            request.session['me'] = me
            return redirect('/')
      else:
         message = ":) Password Do Not Match"
         return redirect('/signup', {"msg":message})
   else:
      return render(request, "register.html")

def account(request):
   return signup(request)

