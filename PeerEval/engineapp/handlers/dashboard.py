from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import webapp2
import jinja2
import os
from handlers import BaseHandler
from models import CourseSection

class Dashboard(BaseHandler):

    def get(self):
        tempValues = self.template_values

        if self.user:
            if self.user_profile:
                #User has profile
                if self.user_profile[0].role == 'student':
                    self.render("dashboard_student.html", self.template_values)
                elif self.user_profile[0].role == 'instructor':
                    qry = CourseSection.query()
                    qry = qry.filter(CourseSection.instructor==self.user)
                    courses = qry.fetch()
                    #tempValues = {}


                    tempValues.update(self.template_values)

                    self.render("dashboard_instructor.html", tempValues)
            else:
                #User does not have profile
                self.redirect("/landing")
        else:
            #pass into template, this should be the destination for the button
            self.url = users.create_login_url(self.request.uri)
            self.url_linktext = 'Login'

    def post(self):
        self.response.write('Submitted')