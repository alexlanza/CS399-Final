from google.appengine.ext import ndb

class CourseSectionRoster(ndb.Model):
	course_section = ndb.KeyProperty(Kind=CourseSection) #Foreign Key Course Section
	user = ndb.UserProperty(repeated=True) #Foreign Key to User