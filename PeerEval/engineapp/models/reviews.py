class Reviews(ndb.Model):

    """A main model for representing an individual User_Login_Name entry."""

    name = ndb.StructuredProperty(Username)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)