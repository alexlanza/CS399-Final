from google.appengine.ext import ndb

class Term(ndb.Model):
	institution = ndb.KeyProperty(Kind=Institution) #Foreign Key to Institution
	term_name = ndb.StringProperty(indexed=False) #example Spring
	term_year = ndb.IntegerProperty() #example 2015
	start_date = ndb.DateTimeProperty() #example 1/11/15
	end_date = ndb.DateTimeProperty()
	#number_of_weeks = ndb.IntegerProperty() #example 16