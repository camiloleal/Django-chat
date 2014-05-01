from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def inicioSesion(request):
	return render_to_response('inicioSesion.html')

def registro(request):
	return render_to_response('registro.html')

def inicio(request):
	return render_to_response('inicio.html')

def grupos(request):
	return render_to_response('grupos.html')

def chatGeneral(request):
	return render_to_response('chatGeneral.html')

def chatGrupo(request):
	return render_to_response('chatGrupo.html')