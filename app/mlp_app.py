# ML Prediction App

# Import flask functionalities to build flask application 
from flask import Flask, request, render_template

# Build flask application
app = Flask(__name__)

# Call method 1: run a hello world application 
@app.route("/login", methods=["GET", "POST"])
# def home():
#     # Check the request code
#     if request.method == "POST":
#         name = request.form["username"]
#         message = f"Hello {name}, POST request received"
#         return message    
#     return render_template("form.html")

# Call method 2: make predictions 
@app.route("/predict", method=["GET", "POST"])
def predict():
    # Check the request 
    if request.method == "POST":
        # predict Brand name 
        brand_name = request.form["brand_name"]

        # predict color
        color_name = request.form["color_name"]

# Test Environment
if __name__ == "__main__":
    app.run(debug=True)

# Call method 2: predict 

