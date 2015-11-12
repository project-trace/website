from django.shortcuts import render, render_to_response
from traceapp import models
from django.views.decorators.http import require_http_methods
from django.forms import ModelForm, BooleanField
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.core.servers.basehttp import FileWrapper
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from subprocess import call
import string
# Create your views here.

#user
@require_http_methods(["POST"])
def loginUser(request):
    username = request.POST['userName']
    password = request.POST['passWord']
    user = authenticate(username=username, password=password)
    if request.user.is_authenticated():
        return render(request, 'already_logged_in.html', {'user_name': request.user.username})
    if user is not None:
        login(request, user)
    else:
        #return render(request,'invalid_login.html')

@require_http_methods(["POST"])
def createUser(request):
    data = request.POST
    try:
        user = User.objects.create_user(username=data['userName'], email=data['email'], password=data['passWord'])
        user.save()
        #return render(request, 'user_created.html')
    except:
       # return render(request, 'invalid_user_creation.html')
