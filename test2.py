import random
import pandas as pd
from difflib import SequenceMatcher

df = pd.read_csv("zoo2.csv")
list_of_questions = list(df.columns[1:])
answers = []

# animals object
class HotAnimal:
    def __init__(self, name, id_list) -> None:
        self.name = name
        self.id_list = id_list

    def get_name(self):
        return self.name
    def get_id(self):
        return self.qid_list

# initiate array of animal objects
sample_animals = []

# pulling animals from df
for animal_name, row in df.iterrows():
    animal_id = row[1:]  # Slice from the second column to the last column
    animal_id_list = list(animal_animal_id_list)

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


####### Overall Process Idea ########## 
# get all answers from first part of each tuple in answers list, and choose animal based on total and which has the most number of the same (true) question IDs

# Ideas: 
#   - way to check database/file (however we're storing info, probably db), and edit animal entries, especially ones made by users
#       - for ex: new animal "beaver" created based on users answers to questions, but as admin you think it necessary to change some answers associated with beaver to be more accurate
#       - sort tuples in list by QID's?
#  