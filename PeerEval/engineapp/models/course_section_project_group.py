from google.appengine.ext import ndb
from models import Project
class ProjectGroup(ndb.Model):
	project = ndb.KeyProperty(Project)#Foriegn Key to Project
	number = ndb.IntegerProperty()
	name = ndb.StringProperty() #Group Name
	max_members = ndb.IntegerProperty()
	