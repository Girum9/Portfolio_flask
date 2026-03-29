from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def homePage():
    return render_template('index.html')
@app.route('/projects')
def projectsPage():
    return render_template('projects.html')
@app.route('/contact')
def contactPage():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)
