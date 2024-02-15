import random
import pandas as pd
from difflib import SequenceMatcher

df = pd.read_csv("zoo2.csv")
list_of_questions = list(df.columns[1:])

answers = []

for questions in list_of_questions:
    print(questions)
    answer = input("True or False? (Enter 1/0): ")
    if answer == "1": 
        answers.append(1)
    else:
        answers.append(0)
print(str(answers) + "    Input")

# animals object
class HotAnimal:
    def __init__(self, name, id_list) -> None:
        self.name = name
        self.id_list = id_list

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id_list

# initiate array of animal objects
sample_animals = []

# pulling animals from df
for animal_name, row in df.iterrows():
    animal_id = row[1:]  # Slice from the second column to the last column
    animal_id_list = list(animal_id)

    name = row[0]

    sample_animals.append(HotAnimal(name, animal_id_list))

# print out animal IDs
# for animal in sample_animals:
#     print(animal.id_list)

# similarity checker
def similarity (a, b):
    return SequenceMatcher(None, a, b).ratio()


# processing to find closest animal
def find_animal (answer):
    best_match = 0
    best_match_animal_name = None
    best_match_id = None

    for animal in sample_animals:
        comparison_result = similarity(animal.get_id(), answer)
        if comparison_result > best_match:
            best_match = comparison_result
            best_match_animal_name = animal.get_name()
            best_match_id = animal.get_id()
            
            # maybe just do best match as a the animal object, and use the methods later for output (saves on a few variables)

    # for displaying numbers
    print(str(best_match_id) + "    ID")
    print('percent closeness: ' + str(best_match))
    return best_match_animal_name

# displaying results
animal_match = find_animal(answers)

if animal_match is not None:  
    print(animal_match)
else:
    print("uhoh spaghettio")

# Other TODOS:
#  - random tiebreaker if animals are still tied
#  - make a guess no matter what
#  - find closest match for first phase of matching, top 3 closest maybe?


# Ideas: 
#   - way to check database/file (however we're storing info, probably db), and edit animal entries, especially ones made by users
#       - for ex: new animal "beaver" created based on users answers to questions, but as admin you think it necessary to change some answers associated with beaver to be more accurate
#       - sort tuples in list by QID's?
#  