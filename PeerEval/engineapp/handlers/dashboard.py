from google.appengine.api import users
from google.appengine.ext import ndb
import urllib
import webapp2
import jinja2
import os
import datetime
import time

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

                    self.response.write(courses)

                    courses.append(tempValues)

                    self.render("dashboard_instructor.html", tempValues)
            else:
                #User does not have profile
                self.redirect("/landing")
        else:
            #pass into template, this should be the destination for the button
            self.url = users.create_login_url(self.request.uri)
            self.url_linktext = 'Login'

    def post(self):
		formname = self.request.get('form_name')
		coursename = self.request.get('course_name')
		coursedescription = self.request.get('course_description')
		termname = self.request.get('term_name')
		begindate = self.request.get('beginDate')
		enddate = self.request.get('endDate')
		#self.response.write(formname + "," + coursename + "," + coursedescription + "," + termname + "," + datetime.datetime.strptime(begindate, "%m/%d/%Y").strftime("%m/%d/%Y") + "," + datetime.datetime.strptime(enddate, "%m/%d/%Y").strftime("%m/%d/%Y"))
		if formname == 'addCourse':
			coursesection = CourseSection(instructor=self.user,name=coursename, description=coursedescription, term_name=termname, begin_date=datetime.datetime.strptime(begindate,"%m/%d/%Y"), end_date=datetime.datetime.strptime(enddate,"%m/%d/%Y"))
			coursesection_key = coursesection.put()
			time.sleep(1)
			self.redirect("/dashboard")