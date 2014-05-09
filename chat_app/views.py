from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def logIn(request):
	return render_to_response('logIn.html')

def signUp(request):
	return render_to_response('signUp.html')

def home(request):
	return render_to_response('home.html')

def groups(request):
	return render_to_response('groups.html')

def generalChat(request):
	return render_to_response('generalChat.html')

def groupChat(request):
	return render_to_response('groupChat.html')