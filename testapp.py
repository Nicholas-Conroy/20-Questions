from flask import Flask, render_template

app = Flask(__name__) # __name__ refers to this file (will be equal to __main__ if file is run from itself, if imported then it is name of file)

@app.route('/') #route for app to follow

def index():
     #knows to check templates folder, just specify file to render
    return render_template("index2.html")

if __name__ == '__main__': 
    app.run(debug=True) #display errors on page, for now