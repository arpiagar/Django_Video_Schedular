

# Create your models here.
import sys
from datetime import datetime, date, timedelta
from django.db import models



class Event(models.Model):
	description = models.TextField('Description')
	File = models.FileField(upload_to='documents/%Y/%m/%d')
	#File = models.TextField('FilePath',max_length=200) 
	schedule = models.DateTimeField('Schedule Time')
	timeout=""
	
	def __unicode__(self):
		return self.description
		


def calcTimeouts(eventlist):
	currdate=datetime.now().utcnow()
	currdate=datetime.strptime(currdate.ctime(), "%a %b %d %H:%M:%S %Y")
	
	print currdate
	for events in eventlist:	
		eventdate=events.schedule+events.schedule.utcoffset()
		eventdate=datetime.strptime(eventdate.ctime(), "%a %b %d %H:%M:%S %Y")
		events.timeout=(((eventdate-currdate).days*86400)+(eventdate-currdate).seconds)*1000
		if events.timeout<0:
			Event.objects.filter(schedule=events.schedule,description=events.description,File=events.File).delete()
	return eventlist