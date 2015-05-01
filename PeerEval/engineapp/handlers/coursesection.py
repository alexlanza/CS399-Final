import webapp2
from handlers import BaseHandler

class CourseSection(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("create_coursesection.html", {})