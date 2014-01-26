from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse

		 
def index(request):

	return HttpResponse("Arpit Your app is Successfully Working.\n \n In order to Schedule Videos go to the admin Page(http://localhost:8011/admin/) \n \n .Once you have set the times for the Videos , go to the url:'http://localhost:8011/schedular/'. \n Note: localhost:8011 signifies that the server is running on port 8011 in my case. ")
	