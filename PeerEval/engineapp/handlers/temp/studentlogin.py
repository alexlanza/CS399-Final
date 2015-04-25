from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import os
import jinja2
import webapp2

# [START login_page]

class LoginPage(webapp2.RequestHandler):

    def get(self):
        user_login = self.request.get('user_login',
                DEFAULT_USER_LOGIN_SYSTEM)
        
        greetings_query = \
            Reviews.query(ancestor=user_login_key(user_login)).order(-Reviews.date)
        
        reviews = greetings_query.fetch(10)

        user = users.get_current_user()
        if user:
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'reviews': reviews,
            'user_login': urllib.quote_plus(user_login),
            'url': url,
            'url_linktext': url_linktext,
            }

        template = JINJA_ENVIRONMENT.get_template('student_login.html')
        self.response.write(template.render(template_values))


# [END login_page]

class User_Login_Name(webapp2.RequestHandler):

    def post(self):

        # We set the same parent key on the 'Review' to ensure each
        # Review is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.

        user_login = self.request.get('user_login',
                DEFAULT_USER_SYSTEM)
        review = Review(parent=user_login_key(user_login))

        if users.get_current_user():
            review.author = \
                Username(name=users.get_current_user().user_id(),
                       email=users.get_current_user().email())

        review.content = self.request.get('content')
        review.put()

        query_params = {'user_login': user_login}
        self.redirect('/?' + urllib.urlencode(query_params))


#app = webapp2.WSGIApplication([('/', MainPage), ('/sign', User_Login_Name)],
#                              debug=True)