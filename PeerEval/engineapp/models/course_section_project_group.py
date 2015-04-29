from google.appengine.ext import ndb

class ProjectGroup(ndb.Model):
	project = ndb.KeyProperty(Kind=Project)#Foriegn Key to Project
	number = ndb.IntegerProperty()
	name = ndb.StringProperty() #Group Name
	