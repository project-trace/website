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


def main():
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
    if request.user.is_authenticated():
        #return render(request, 'already_logged_in.html', {'user_name': request.user.username})
		return "OK";
    if user is not None:
        login(request, user)
    else:
        #return render(request,'invalid_login.html')
		return "OK";

if __name__=="__main__": main()
