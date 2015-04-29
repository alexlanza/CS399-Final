from google.appengine.ext import ndb

class CoursesSection(ndb.Model):
	name = ndb.StringProperty()
	course = ndb.KeyProperty(Kind=Course) #Foreign Key Course
	term = ndb.KeyProperty(Kind=Term) #Foreign Key to Term
	