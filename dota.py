# Import the Flask class and the render_template function from the flask module.
# Flask lets us create a web application.
# render_template helps us connect Python code to an HTML file (like index.html).
from flask import Flask, render_template
from datetime import datetime
import pytz

# Create an instance of the Flask web application.
# '__name__' tells Flask where to look for things like templates and static files.
dota = Flask(__name__)

# Define a route — this means:
# "When someone goes to the homepage (URL path '/'), run this function below."
@dota.route("/")
def home():
    # Set Kuwaiti timezone
    kuwait_tz = pytz.timezone('Asia/Kuwait')

     # Get current time in Kuwait
    now_kuwait = datetime.now(kuwait_tz)

    # Format the date/time
    formatted_time = now_kuwait.strftime("%A, %B %d, %Y – %I:%M %p")

    # Render the HTML file 'index.html' and pass a variable 'name' with the value "Fatma"
    # That variable will be used inside the HTML using {{ name }}
    return render_template("index.html", name="Fatma", current_time=formatted_time)

# This says: "Only run the app if this file is being run directly (not imported from somewhere else)"
if __name__ == "__main__":
    # Start the Flask development server.
    # 'debug=True' means:
    # - If your code has an error, it will show a detailed error page.
    # - If you change your code, the app automatically restarts (you don't have to restart the server yourself).
    dota.run(debug=True)