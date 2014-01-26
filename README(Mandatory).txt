Stpes for Running the setup.


1. Create the database :
		Command:python manage.py syncdb
		
		
2. Start the server on port 8011: 
		Command: python manage.py runserver 8011
		
3. Open the Url: http://localhost:8011/
		Verifies that the project works.
		
4. Open the Url: http://localhost:8011/admin/
		4.1 Login using the DB credentials.
		4.2 Add and Event.
				4.2.1. Add event description,
				4.2.2. Select a .mp4 file (PS: I have not implemented any check so that it uploads only .mp4. So user must ensure that the file he/she uploads is in .mp4 format).
				4.2.3. Add the event DateTime
				4.2.4 Click on Save button.
				
5.	As soon as you add the series of events, go to URL: http://localhost:8011/schedular/
			5.1 It will display the events present in DB, their info and the time(in ms) in which they will occur.
			5.2 On the event time, a new browser window will be opened, and the video will be played in JW player.
			

Programming Problem Complete!!
