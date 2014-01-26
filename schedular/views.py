# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response	
from schedular import models
from finalproject import settings 
from django.shortcuts import render
import os



def playVideo(request,event_id,template='PlayPlayer.html'):
	queue=models.Event.objects.order_by( 'schedule' )
	try:
		eventobj=models.Event.objects.filter(pk=event_id)	
		if eventobj!=[]:
			fileurl=eventobj[0].File
			queue=models.calcTimeouts(queue) # Fetching the queue again so that the event whose timeout is hit and for which video is being played will get deleted from DB at the time of timout itself.Will not have to wait for Refresh of /schedular/ page.
			return render(request, template, {'fileurl': fileurl},content_type="text/html")
	except: #Providing the handler when the user deletes the event using Django Administration before the event actually occurs.
		return render(request,'404.html',content_type="text/html")
	
def listEvents(request,template='player.html'):
	queue=models.Event.objects.order_by( 'schedule' )
	print "queue",queue
	queue=models.calcTimeouts(queue)
	return render(request, template, {'eventlist': queue},content_type="text/html")
	

		
		