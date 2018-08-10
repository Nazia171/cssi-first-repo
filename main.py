#main.py
import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions =['jinja2.ext.autoescape'],
    autoescape=True)


class HomePage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(home_template.render())


app= webapp2.WSGIApplication([
    ('/', HomePage)
], debug=True)
