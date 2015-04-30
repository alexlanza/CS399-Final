import webapp2
from handlers import BaseHandler

class Index(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("index.html", self.template_values)