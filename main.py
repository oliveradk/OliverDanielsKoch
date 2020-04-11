from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap

nav = Nav()

# registers the "top" menubar
nav.register_element('top', Navbar(
    View('Oliver Daniels-Koch', 'homepage'),
    Link('GITHUB', 'https://github.com/oliveradk'),
    Link('LINKEDIN',"https://www.linkedin.com/in/oliver-daniels-koch-b87ab3178/"),
    View('BLOG', 'blog')
))

app = Flask(__name__)
Bootstrap(app)
nav.init_app(app)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
