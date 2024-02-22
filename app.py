from flask import Flask, render_template, request, jsonify
import prg

app = Flask(__name__) # __name__ refers to this file (will be equal to __main__ if file is run from itself, if imported then it is name of file)

#create dataframe of existing animals in csv 
#TODO make sure this reloads the csv on every page load
animals_df = prg.read_csv("zoo2.csv")

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
        
        list_of_animals = prg.get_animals_list(animals_df)
        
        best_animal_name = prg.find_animal(list_of_animals, answers_list)
        
        print(best_animal_name)
                
        return {'total': best_animal_name}
    else:
        return 'Go away'
    
@app.route('/data') #user can go to this route and see the data
def data():
    questions_data = prg.return_questions(animals_df)
    return {"data" : questions_data}

# this route is used to add a new animal to the csv, if it does not already exist in the file
@app.route('/addAnimal', methods=['GET', 'POST'])
def addAnimal():
    
    if request.method == 'POST':
        global animals_df
        data = request.get_json()
        print(data)
        
        # formats animal name so it is added to CSV in lowercase
        data['animal'] = data['animal'].lower()
        
        # add animal and answers list to csv, if not already in csv
        animal_added = prg.append_to_csv(data['animal'], data['answers'], animals_df)
        
        if animal_added:
            animals_df = prg.read_csv("zoo2.csv") #reread csv and update global variable so data is up to date when page is refreshed
            return {'message' : 'New animal added!'}
        else:
            return {'message' : 'This animal is already in the system. We must have guessed wrong, sorry.'}
    else:
        return "Go away"
    
if __name__ == '__main__': 
    app.run(debug=True) #display errors on page, for now