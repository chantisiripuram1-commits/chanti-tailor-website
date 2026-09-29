from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


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

        return """
        <h1>Order Submitted Successfully!</h1>
        <p>Thank you for choosing Chanti Tailor.</p>
        <a href="/">Go Back Home</a>
        """

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

        email = request.form.get("email")
        password = request.form.get("password")

        print("Login Email:", email)
        print("Login Password:", password)

        return """
        <h1>Login Submitted!</h1>
        <p>Login system will be connected to MySQL later.</p>
        <a href="/">Go Back Home</a>
        """

    return render_template("login.html")


# =====================================
# SIGNUP
# =====================================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check passwords
        if password != confirm_password:

            return """
            <h1>Passwords do not match!</h1>
            <a href="/signup">Try Again</a>
            """

        print("Name:", name)
        print("Email:", email)

        return f"""
        <h1>Signup Successful!</h1>

        <h2>Welcome, {name}!</h2>

        <p>Your account has been created successfully.</p>

        <p>Email: {email}</p>

        <br>

        <a href="/login">Go to Login</a>

        <br><br>

        <a href="/">Go Back Home</a>
        """

    # If user simply opens /signup
    return render_template("signup.html")
# =====================================
# RUN APPLICATION
# =====================================

if __name__ == "__main__":
    app.run(debug=True)