#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from chat_app.forms import *
from chat_app.models import *

def logIn(request):
    login(request, user)
    return render_to_response('chat_app/logIn.html')

def signUp(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        registered = False

        if user_form.is_valid(): 
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
            email = user_form.cleaned_data["email"]
            
            user = User.objects.create_user(username, email, password)            
            user.save()

            registered = True
            
            return render_to_response('chat_app/signUp.html', 
            	{'user_form': user_form, 'registered': registered})
    else:
        user_form = UserForm()
 
    data = {'user_form': user_form,}
    
    return render_to_response('chat_app/signUp.html', 
        data, context_instance=RequestContext(request))

@login_required()
def home(request):
    return render_to_response('chat_app/home.html', 
        {'user': request.user}, context_instance=RequestContext(request))