from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import webapp2
import jinja2
import os
from handlers import BaseHandler
from models import UserProfile
 
class Landing(BaseHandler):

    def get(self):
		if self.user:
			if self.user_profile:
				#User has profile
				self.redirect("/dashboard")
			else:
				#User does not have profile
				self.render("landing.html", self.template_values)
		else:
            #pass into template, this should be the destination for the button
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
    
    def post(self):
		self.user = users.get_current_user()
		if self.user:
			selectedrole = self.request.get('role')
			if selectedrole == 'student':
				self.response.out.write('Student')
				userprofile = UserProfile(user=self.user, role=selectedrole)
				userprofile_key = userprofile.put()
				self.redirect("/dashboard")
			elif selectedrole == 'instructor':
				self.response.out.write('Instructor')
				userprofile = UserProfile(user=self.user, role=selectedrole)
				userprofile_key = userprofile.put()
				self.redirect("/dashboard")
			else:
				self.response.out.write('Error. Did not get expected role')
		else:
			self.url = users.create_login_url(self.request.uri)
			self.url_linktext = 'Login'
