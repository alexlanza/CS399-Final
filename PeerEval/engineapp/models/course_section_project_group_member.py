from google.appengine.ext import ndb
from models import ProjectGroup
class ProjectGroupMember(ndb.Model):
	project_group = ndb.KeyProperty(ProjectGroup)#Foriegn Key to ProjectGroup
	user = ndb.UserProperty(repeated=True) #Foreign Key to Users