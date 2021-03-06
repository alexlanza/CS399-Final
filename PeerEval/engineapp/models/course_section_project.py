from google.appengine.ext import ndb
from models import CourseSection
class Project(ndb.Model):
	name = ndb.StringProperty()
	course_section = ndb.KeyProperty(CourseSection) #Foreign Key Course Section
	eval_open_date = ndb.DateProperty()
	eval_close_date = ndb.DateProperty() 
	group_formation = ndb.StringProperty() #Instructor Assign / Student Self Assign
