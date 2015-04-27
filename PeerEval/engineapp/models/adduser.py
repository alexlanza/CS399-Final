from google.appengine.ext import ndb

class addUser(ndb.Model):

    """Sub model for representing a user."""

    class = ndb.StringProperty(indexed=False)
    user = ndb.StringProperty(indexed=False)