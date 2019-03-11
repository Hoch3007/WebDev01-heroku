from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
            {'author' : 'Hoch3007', 'title' : 'Blog Post 1', 'content' :'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.', 'date_posted': 'March, 1st 2019'},
    {'author': 'Hoch3007', 'title': 'Blog Post 2',
     'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
     'date_posted': 'March, 2st 2019'}
]


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')


@app.route("/portfolio/fakebook")
def fakebook():
    return "Fakebook"


@app.route("/portfolio/boogle")
def boogle():
    return "Boogle"

@app.route("/blog")
def blog():
    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)



