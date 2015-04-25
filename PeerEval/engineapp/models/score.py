from google.appengine.ext import ndb

class Score(ndb.Model):
score = ndb.IntegerProperty()