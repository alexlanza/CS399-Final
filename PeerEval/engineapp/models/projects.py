from google.appengine.ext import ndb

class Projects(ndb.Model):

    """A main model for representing an individual User_Login_Name entry."""

    name = ndb.StringProperty(Username)
    due_date = ndb.DateTimeProperty(auto_now_add=True)