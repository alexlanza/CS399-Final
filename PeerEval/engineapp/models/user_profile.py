from google.appengine.ext import ndb

class UserProfile(ndb.Model):
	user = ndb.UserProperty(repeated=False) #Foreign Key to User
	role = ndb.StringProperty(indexed=False) #Instructor, Student, Admin
	institution = ndb.KeyProperty(Kind=Institution) #Foreign Key to Institution