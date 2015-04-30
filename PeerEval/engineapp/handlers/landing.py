from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import webapp2
import jinja2
import os
from handlers import BaseHandler

class Landing(BaseHandler):

    def get(self):
        user = users.get_current_user()
        if user:
            #have a button with logout on main page
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            #pass into template, this should be the destination for the button
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            }
        self.render("landing.html", (template_values))
    
    def post(self):
        user_login = self.request.get('user_login',
                'DEFAULT_USER_SYSTEM')
        
        query_params = {'user_login': user_login}
        self.redirect('/?' + urllib.urlencode(query_params))