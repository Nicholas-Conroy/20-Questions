import random
import pandas as pd
from difflib import SequenceMatcher

df = pd.read_csv("zoo2.csv")

# fix legs column later, dont forget
df = df.drop(["legs","class_type","catsize","fins","venomous","tail","domestic"], axis=1)

# print(df.head())

list_of_questions = list(df.columns)

# print(list_of_questions)

# index = random.shuffle(list_of_questions)

answers = []

# Appends answers into answers array as 0s or 1s
for questions in list_of_questions:
    print(questions)
    answer = input("True or False? (Enter 1/0): ")
    if answer == "1": 
        answers.append(int(answer))
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

# Pulls animals from df
for animal_name, row in df.iterrows():
    animal_QID = row[1:]  # Slice from the second column to the last column
    iD = list(animal_QID)
    name = row[0]
    
    true_sum = sum(animal_QID)

    sample_animals.append(HotAnimal(name,true_sum,iD))

# print out animas IDs
# for animal in sample_animals:
    # print(animal.get_id())
###################################################


#returns the amount of correct QIDs for a given sample


def similarity (a, b):
    return SequenceMatcher(None, a, b).ratio()

#Processing for comparisons
def find_animal (answer):
    for animals in HotAnimal:
        similarity (HotAnimal.get_id(), answer)



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