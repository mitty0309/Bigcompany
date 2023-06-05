from django.shortcuts import render
from django.http import HttpResponse

def bigcompany(request):
	# return HttpResponse("Hello World")
	return render(request, 'bigcompany.html')