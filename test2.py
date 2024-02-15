import random
import pandas as pd
from difflib import SequenceMatcher

df = pd.read_csv("zoo2.csv")
# df = df.drop(["legs","class_type","catsize","fins","venomous","tail","domestic"], axis=1)

# include all the columns except the first (animal_names)
list_of_questions = list(df.columns[1:])
# index = random.shuffle(list_of_questions)

answers = []

# Appends answers into answers array as 0s or 1s
for questions in list_of_questions:
    print(questions)
    answer = input("True or False? (Enter 1/0): ")
    if answer == "1": 
        answers.append(1)
    else:
        answers.append(0)
print(answers)

###################################################
# sample animal has key of number of "True"s and value of list of which QIDs are true for it
class HotAnimal:
    def __init__(self, name, num_true, qid_list) -> None:
        self.name = name
        self.num_true = num_true
        self.qid_list = qid_list
    
    def get_name(self):
        return self.name
    def get_id(self):
        return self.qid_list
###################################################
sample_animals = []

# Pulls animals from df
for animal_name, row in df.iterrows():
    animal_QID = row[1:]  # Slice from the second column to the last column
    iD = list(animal_QID)
    name = row[0]
    true_sum = sum(animal_QID)

    sample_animals.append(HotAnimal(name,true_sum,iD))
# print out animas IDs
# for animal in sample_animals:
#     print(animal.get_id())
###################################################
def similarity (a, b):
    return SequenceMatcher(None, a, b).ratio()

#Processing for comparisons

# best_animal:HotAnimal = None
def find_animal (answer):
    best_match = 0
    animal_match = None
    for animal in sample_animals:
        result = similarity(animal.get_id(), answer)
        if result > best_match:
            best_match = result
            animal_match = animal.get_name()

    return animal_match
# make animal_matches a list of tuples, where one val is the 
# but wait how does that sort, might have to be more manual
# theres also ways to just keep track 

joe = find_animal(answers)

if joe is not None:  
    print(joe)
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