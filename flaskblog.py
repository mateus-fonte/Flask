from flask import Flask, render_template, url_for
app = Flask(__name__) # Initializing our web application trough the app variable

posts = [               # A list of Dictionaries that we will loop trough
    {
        "author": "Corey Schafer",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 20, 2018"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "April 21, 2018"
    }
]

@app.route("/")         # Creating a route to our main page
@app.route("/home")     # Another route to the same page
def home():
    return render_template("home.html", posts=posts)    # Instead of writing the whole html here we can simply use a template, and pass variables like the posts 

@app.route("/about")
def about():
    return render_template("about.html", title="about") # Now we are passing a title variable, that will be test in the about template to check if there is a title already

if __name__ == "__main__":
    app.run(debug=True, port=9000)