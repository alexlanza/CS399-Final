import webapp2
from handlers import BaseHandler

class InstructorDashboard(BaseHandler):
    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.render("dashboard_instructor.html", {})
		

#Can add course section
#can add students (to course section) 
	#Should check if student exists in user_profile model
		#if does not exist add student to user_profile model
#Can add project (to course section)
#Can add/remove user from project group
#Can add/remove group slots
	#On remove group slot check if membership is empty



