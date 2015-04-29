from google.appengine.ext import ndb

class ProjectGroupScore(ndb.Model):
	project_group = ndb.KeyProperty(Kind=ProjectGroup)#Foriegn Key to ProjectGroup
	user = ndb.UserProperty(repeated=True) #Foreign Key to Users
	eval_user = ndb.UserProperty(repeated=True) #Foreign Key to Users
	score = ndb.IntegerProperty() #Score