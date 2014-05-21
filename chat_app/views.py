from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from chat_app.forms import *
from chat_app.models import *


def logIn(request):	
	return render_to_response('chat_app/logIn.html')

def signUp(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = ProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save

			ChatProfile = profile_form.save(commit=False)
			ChatProfile.user = user
			
			registered = True

		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = ProfileForm()

	return render_to_response('chat_app/signUp.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)
	
@login_required()
def home(request):
    return render_to_response('chat_app/home.html', {'user': request.user}, context_instance=RequestContext(request))