from google.appengine.api import users
import webapp2
import jinja2
import os
from models import UserProfile

jinja_environment = jinja2.Environment(
        extensions=['jinja2.ext.autoescape'],
        loader=jinja2.FileSystemLoader(
            os.path.dirname(__file__) + "/../templates/"),
        autoescape=True)

class BaseHandler(webapp2.RequestHandler):

    def __init__(self, request=None, response=None):
		super(BaseHandler, self).__init__(request, response)
		# your own code goes here...
		self.user = users.get_current_user()
		if self.user:
			qry = UserProfile.query()
			qry = qry.filter(UserProfile.user==self.user)
			self.user_profile = qry.fetch()

			self.url = users.create_logout_url(self.request.uri)
			self.url_linktext = 'Logout'
			self.template_values = {
			'user': self.user,
			'url': self.url,
			'url_linktext': self.url_linktext,
			}
		else:
            #pass into template, this should be the destination for the button
			self.url = users.create_login_url(self.request.uri)
			self.url_linktext = 'Login'

    def render(self, template_name, template_values):
        template = jinja_environment.get_template(template_name)
        self.response.out.write(template.render(template_values))

