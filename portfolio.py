from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# API for the home page
@app.route('/')
def index():
    return render_template('index.html')


# API for the about page
@app.route('/about')
def about():
    return render_template('about.html')


# API for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0",port=5000)