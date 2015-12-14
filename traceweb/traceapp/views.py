from django.shortcuts import render, render_to_response
from traceapp.models import Device
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
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db import models
import string


# Create your views here.

def ajax_registration(request):
    obj = {
        'login_form': AuthenticationForm(),
        'user_creation_form': UserCreationForm(),
    }
    return render(request, 'ajax_registration.html', obj)


#user
def loginUser(request):
	username = request.GET.get('username')
	password = request.GET.get('password')
	user = authenticate(username=username, password=password)
	if user is None:
		return HttpResponse('invalid')
	else:
		login(request,user)
		return HttpResponse('valid')

def signUp(request):
	first_name = request.GET.get('first_name')
	last_name = request.GET.get('last_name')
	username = request.GET.get('username')
	password = request.GET.get('password')
	try:
		user = User.objects.create_user(username, "", password)
		user.last_name = last_name
		user.first_name = first_name
		user.save()
		return HttpResponse('valid')
	except:
		return HttpResponse('invalid')

def regItem(request):
	itemName = request.GET.get('itemName')
	itemID = request.GET.get('itemID')
	if(itemName=="" or itemID==""):
		return HttpResponse('invalid')
	try:
		device = Device.objects.create(name=itemName, device_id=itemID)
		device.save();
		return HttpResponse('valid')
	except:
		return HttpResponse('invalid')

def home(request, userId):
	query_results = Device.objects.all()
	return render(request, 'home.html', {'username': request.user.username, 'query_results': query_results})

def logout(request):
	auth.logout(request)
	return render(request, 'logout.html')

def loginHome(request):
	if(request.user.username !=""):
		query_results = Device.objects.all()
		return render(request, 'home.html', {'username': request.user.username, 'query_results': query_results})
	return render(request, 'login.html')

