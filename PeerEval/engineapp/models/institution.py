from google.appengine.ext import ndb

class Institution(ndb.Model):
	institution_name = ndb.StringProperty(indexed=False) #Example = Northern Arizona University
	state = ndb.StringProperty(indexed=False)
	country = ndb.StringProperty(indexed=False)
	email_domain = ndb.StringProperty(indexed=False) #example nau.edu
	