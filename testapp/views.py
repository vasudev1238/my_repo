from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
	s='<h1>Hello Students welcome to DURGASOFT Django classes!!!</h1>'
	return HttpResponse(s)


