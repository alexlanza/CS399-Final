from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import webapp2
import jinja2
import os

from handlers import BaseHandler
#from models import reviews, username

class InstructorLogin(BaseHandler):

    def get(self):
        user_login = self.request.get('user_login',
                'DEFAULT_USER_LOGIN_SYSTEM')

        #greetings_query = \
        #    Reviews.query(ancestor=user_login_key(user_login)).order(-Reviews.date)

        #reviews = greetings_query.fetch(10)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            #'reviews': reviews,
            'user_login': urllib.quote_plus(user_login),
            'url': url,
            'url_linktext': url_linktext,
            }
        self.render("instructor_login.html", {})
		
#class User_Login_Name(BaseHandler):

    def post(self):

        # We set the same parent key on the 'Review' to ensure each
        # Review is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.

        user_login = self.request.get('user_login',
                'DEFAULT_USER_SYSTEM')
        #review = Review(parent=user_login_key(user_login))

        #if users.get_current_user():
        #    review.author = \
        #        username(name=users.get_current_user().user_id(),
        #               email=users.get_current_user().email())

        #review.content = self.request.get('content')
        #review.put()

        query_params = {'user_login': user_login}
        self.redirect('/?' + urllib.urlencode(query_params))