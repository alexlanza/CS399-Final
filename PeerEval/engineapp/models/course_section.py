from google.appengine.ext import ndb

class CourseSection(ndb.Model):
	name = ndb.StringProperty() #Example CS399
	description = ndb.StringProperty() #Example Advanced Web Programming
	instructor = ndb.UserProperty() #Foreign Key to User
	term_name = ndb.StringProperty() #Example Spring 2015
	begin_date = ndb.DateProperty()
	end_date = ndb.DateProperty()
