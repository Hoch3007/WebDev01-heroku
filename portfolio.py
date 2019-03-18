from flask import Flask, render_template, url_for, request, redirect, flash, make_response
from random import randint


app = Flask(__name__)
app.secret_key = '6ca97bc342cdbecabbadb5c47b006ef4'

posts = [
            {'author' : 'Hoch3007', 'title' : 'Blog Post 1', 'content' :'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.', 'date_posted': 'March, 1st 2019'},
    {'author': 'Hoch3007', 'title': 'Blog Post 2',
     'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
     'date_posted': 'March, 2nd 2019'},
    {'author': 'Hoch3007', 'title': 'Blog Post 3',
     'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
     'date_posted': 'April, 1st 2019'},
{'author': 'Hoch3007', 'title': 'Blog Post 4',
     'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
     'date_posted': 'May, 21st 2019'},
{'author': 'Hoch3007', 'title': 'Blog Post 5',
     'content': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.',
     'date_posted': 'June, 12th 2019'}
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


@app.route("/blog")
def blog():
    return render_template('blog.html', posts=posts)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    contact_name = request.form.get("name")
    contact_text = request.form.get("text_message")

    print(contact_name)
    print(contact_text)

    if request.method == "POST":
        response = make_response(render_template("success.html"))
        #response = make_response(redirect("contact.html"))
        response.set_cookie("user_name", contact_name)
        #flash("Great! Thank you. Your message was sent.", 'success')
        #return redirect('/contact')
        return response
    else:
        user_name = request.cookies.get("user_name")
        return render_template('contact.html', name=user_name)


@app.route("/game", methods=["GET", "POST"])
def guess():

    number_guess = request.form.get("guess")

    if request.method == "POST":

        secret_number = request.cookies.get("secret_number")

        # flask app akzeptiert bei Cookies keine Integer
        if int(secret_number) == int(number_guess):
            response = make_response(render_template("result.html"))
            # expires funktioniert nicht
            response.set_cookie("secret_number", max_age=0)
            return response

        else:

            if int(secret_number) > int(number_guess):
                #direction = "higher"
                flash("Sorry, that's not correct. Your guess "+ str(number_guess) + " is too low. Guess again!", 'danger')
            else:
                #direction = "lower"
                flash("Sorry, that's not correct. Your guess " + str(number_guess) + " is too high. Guess again!", 'danger')
            #return render_template("error.html", direction=direction)
            return redirect("/game")

    elif request.method == "GET":

        secret_number = request.cookies.get("secret_number")

        if secret_number is None:

            number = randint(0, 30)
            response = make_response(render_template("game.html"))
            response.set_cookie("secret_number", str(number))

            return response
        else:

            return render_template('game.html')


if __name__ == '__main__':
    app.run(debug=True)



