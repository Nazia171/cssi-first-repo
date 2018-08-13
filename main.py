#main.py
import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions =['jinja2.ext.autoescape'],
    autoescape=True)


class homePage(webapp2.RequestHandler):
    def get(self):
        home_template = the_jinja_env.get_template('index.html')
        self.response.write(home_template.render())



class musicPage(webapp2.RequestHandler):
    def get(self):
        music_template = the_jinja_env.get_template('music.html')
        self.response.write("HIIIII")

app= webapp2.WSGIApplication([
    ('/', homePage),
    ('/music', musicPage)
], debug=True)
