from flask import Flask, render_template

app = Flask(__name__)


# Index ---------------------------------------------------------------------

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e: 
        return str(e)

""" @app.route("/cv")

def display_grid():
    try:    
        return render_template("cv.html")

    except Exception as e:
        return str(e) """

if __name__ == "__main__":
    app.run(debug=True)