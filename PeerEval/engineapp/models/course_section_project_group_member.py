from google.appengine.ext import ndb

class ProjectGroupMember(ndb.Model):
	project_group = ndb.KeyProperty(Kind=ProjectGroup)#Foriegn Key to ProjectGroup
	user = ndb.UserProperty(repeated=True) #Foreign Key to Users