from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.conf import settings
import datetime,os
time = datetime.datetime.now()
time = time.strftime("%H:%M:%S")
User = get_user_model()
# Create your views here.

def home(request):
   if request.method == "POST":
      pass
   else:
     return render(request, "studio.html")

def post(request):
   pass

def edit_post(request):
   pass
