from flask import Flask, render_template, request, jsonify

app = Flask(__name__) # __name__ refers to this file (will be equal to __main__ if file is run from itself, if imported then it is name of file)

#route for app to follow, this triggers the following function (the '/'indicates this is for the root url)
@app.route('/') 
def index():
     #knows to check templates folder, just specify file to render
    return render_template("index2.html")
    
@app.route('/process', methods=['GET', 'POST'])
def process():
    
    if request.method == 'POST':
        print('incoming POST')
        data = request.get_json()
        answers_list = data['answers']
        print(answers_list)
        
        #just testing things out
        num_of_answers = len(answers_list)
        # print(type(data['greeting']))
        
        return {'total': num_of_answers}
    else:
        return 'Go away'
    
@app.route('/data') #user can go to this route and see the data
def data():
    return {"data" : [
        "hair","feathers","eggs","milk","airborne","aquatic","predator",
        "toothed","backbone","breathes","venomous","fins","tail","domestic","legless","quadruped"
    ]}

if __name__ == '__main__': 
    app.run(debug=True) #display errors on page, for now