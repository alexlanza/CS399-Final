from google.appengine.ext import ndb
from models import CourseSection
class CourseSectionRoster(ndb.Model):
	course_section = ndb.KeyProperty(CourseSection) #Foreign Key Course Section
	user = ndb.UserProperty(repeated=True) #Foreign Key to User