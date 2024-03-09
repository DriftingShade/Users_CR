from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_user", methods=["POST"])
def create_user():

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect("/show_user")


@app.route("/users")
def show_users():
    users = User.get_all()

    return render_template("users.html", all_users=users)


@app.route("/edit_user")
def edit_user():
    User.update(request.form)
    return redirect("/show_user")


@app.route("/show_user")
def one_user():
    return render_template("single_user.html")


if __name__ == "__main__":
    app.run(debug=True)
