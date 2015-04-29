from google.appengine.ext import ndb

class Project(ndb.Model):
    name = ndb.StringProperty()
	course_section = ndb.KeyProperty(Kind=CourseSection) #Foreign Key Course Section
	eval_open_date = ndb.DateProperty()
	eval_close_date = ndb.DateProperty() 
	group_formation = ndb.StringProperty() #Instructor Assign / Student Self Assign
	
	#due_weeknumber = ndb.IntegerProperty()
	#due_weekday = ndb.IntegerProperty()
	#Calculated field DueDate