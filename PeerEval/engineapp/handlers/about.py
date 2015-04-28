import webapp2
from handlers import BaseHandler

class About(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("about.html", {})