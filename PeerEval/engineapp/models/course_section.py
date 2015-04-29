from google.appengine.ext import ndb

class CoursesSection(ndb.Model):
	name = ndb.StringProperty() #Example CS399
	description = ndb.StringProperty() #Example Advanced Web Programming
	term_name = ndb.StringProperty() #Example Spring 2015
	begin_date = ndb.DateProperty()
	end_date = ndb.DateProperty()
