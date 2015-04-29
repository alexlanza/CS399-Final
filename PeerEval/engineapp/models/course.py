from google.appengine.ext import ndb
import Institution

class Course(ndb.Model):
	name = ndb.StringProperty()
	decription = ndb.StringProperty()
	institution = ndb.KeyProperty(Kind=Institution) #Foreign Key to Institution
	