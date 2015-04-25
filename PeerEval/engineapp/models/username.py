from google.appengine.ext import ndb

class Username(ndb.Model):

    """Sub model for representing a user."""

    name = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    password = ndb.StringProperty(indexed=False)