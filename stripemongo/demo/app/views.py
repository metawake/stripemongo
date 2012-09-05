import json
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import Connection
from stripemongo import stripemongo

@csrf_exempt
@stripemongo
def index(request):
	
	return HttpResponse(status=200)