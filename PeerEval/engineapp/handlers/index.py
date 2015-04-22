import webapp2
#from models import MartianPizza
from handlers import BaseHandler


class Index(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("index.html", {})

class InstructorHome(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("instructor_home.html", {})