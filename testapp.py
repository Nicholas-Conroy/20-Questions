from flask import Flask, render_template, request, jsonify
import minitest as mt

app = Flask(__name__) # __name__ refers to this file (will be equal to __main__ if file is run from itself, if imported then it is name of file)

#create dataframe of existing animals in csv 
#TODO make sure this reloads the csv on every page load
animals_df = mt.read_csv("zoo2.csv")

# print(animals_df.head())

#route for app to follow, this triggers the following function (the '/'indicates this is for the root url)
@app.route('/') 
def index():
     #knows to check templates folder, just specify file to render
    return render_template("index.html")
    
@app.route('/process', methods=['GET', 'POST'])
def process():
    
    if request.method == 'POST':
        print('incoming POST')
        data = request.get_json()
        answers_list = data['answers']
        # print(answers_list)
        
        list_of_animals = mt.get_animals_list(animals_df)
        
        best_animal_name = mt.find_animal(list_of_animals, answers_list)
        
        print(best_animal_name)
                
        return {'total': best_animal_name}
    else:
        return 'Go away'
    
@app.route('/data') #user can go to this route and see the data
def data():
    questions_data = mt.return_questions(animals_df)
    return {"data" : questions_data}

@app.route('/addAnimal', methods=['GET', 'POST'])
def addAnimal():
    
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        
        # formats animal name so it is added to CSV in lowercase
        data['animal'] = data['animal'].lower()
        
        # add animal and answers list to csv
        mt.append_to_csv(data['animal'], data['answers'])
        
        return {'message' : 'New animal added!'}
    else:
        return "Go away"
    
if __name__ == '__main__': 
    app.run(debug=True) #display errors on page, for now