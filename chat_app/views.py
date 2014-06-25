#from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from chat_app.forms import *
from chat_app.models import *
from chat_app.student import *
from chat_app.store import *
from chat_app.update import *

vector = []
update = Update(vector)
update.start()

def logIn(request):
    store = Store()
    store.save_data(vector)
    login(request, user)
    return render_to_response('chat_app/logIn.html')


def signUp(request):
    vector = update.get_vector()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        registered = False

        if user_form.is_valid(): 
            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]
            email = user_form.cleaned_data["email"]
            student = Student()
            student.set_username(username)
            student.set_password(password)
            student.set_email(email)
            vector.append(student)
            print vector
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
    registered_users = User.objects.all()

    return render_to_response('chat_app/home.html', 
        {'user': request.user, 'registered_users': registered_users}, context_instance=RequestContext(request))
