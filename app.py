from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "chanti-tailor-secret-key"


# =====================================
# HOME
# =====================================

@app.route("/")
def home():
    return render_template("home.html")


# =====================================
# ABOUT
# =====================================

@app.route("/about")
def about():
    return render_template("about.html")


# =====================================
# SERVICES
# =====================================

@app.route("/services")
def services():
    return render_template("services.html")


# =====================================
# CATALOGUE
# =====================================

@app.route("/catalogue")
def catalogue():
    return render_template("catalogue.html")


# =====================================
# CUSTOM DESIGN
# =====================================

@app.route("/custom-design")
def custom_design():
    return render_template("custom_design.html")


# =====================================
# PLACE ORDER
# =====================================

@app.route("/place-order", methods=["GET", "POST"])
def place_order():

    if request.method == "POST":

        name = request.form.get("name")
        phone = request.form.get("phone")
        product = request.form.get("product")

        print("Customer Name:", name)
        print("Phone:", phone)
        print("Product:", product)

        flash("Order placed successfully!", "success")

        return redirect(url_for("place_order"))

    return render_template("place_order.html")


# =====================================
# MY ORDERS
# =====================================

@app.route("/my-orders")
def my_orders():
    return render_template("my_orders.html")


# =====================================
# CONTACT
# =====================================

@app.route("/contact")
def contact():
    return render_template("contact.html")


# =====================================
# LOGIN
# =====================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        session["user"] = email

        return redirect("/")

    return render_template(
        "login.html",
        user=session.get("user")
    )


# =====================================
# SIGNUP
# =====================================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # For now, just store the user's name in session
        session["user"] = name

        return redirect("/")

    return render_template(
        "signup.html",
        user=session.get("user")
    )


# =====================================
# LOGOUT
# =====================================

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")


# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    app.run(debug=True)  
