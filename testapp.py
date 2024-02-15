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
        
        
        #just testing things out
        num_of_answers = len(answers_list)
        # print(type(data['greeting']))
        
        return {'total': num_of_answers}
    else:
        return 'Go away'
    
    

if __name__ == '__main__': 
    app.run(debug=True) #display errors on page, for now