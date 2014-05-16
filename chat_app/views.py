from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def logIn(request):
	return render_to_response('chat_app/logIn.html')

def signUp(request):
	return render_to_response('chat_app/signUp.html')

def home(request):
	return render_to_response('chat_app/home.html')

def groups(request):
	return render_to_response('chat_app/groups.html')

def generalChat(request):
	return render_to_response('chat_app/generalChat.html')

def groupChat(request):
	return render_to_response('chat_app/groupChat.html')