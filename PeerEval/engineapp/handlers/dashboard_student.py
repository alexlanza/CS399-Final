import webapp2
from handlers import BaseHandler

class StudentDashboard(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("dashboard_student.html", {})
		
#Can select institution?
#View assigned Course sections
#View course section projects
#View assigned groups
#Self assign to group