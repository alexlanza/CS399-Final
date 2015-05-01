from google.appengine.ext import ndb
from models import CourseSection
class CourseSectionRoster(ndb.Model):
	course_section = ndb.KeyProperty(CourseSection) #Foreign Key Course Section
	email = ndb.TextProperty()