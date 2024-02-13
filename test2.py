import random
import pandas as pd

df = pd.read_csv("zoo2.csv")

# fix legs column later, dont forget
df = df.drop(["legs","class_type","catsize","fins","venomous","tail","domestic"], axis=1)

print(df.head())

list_of_questions = list(df.columns)

print(list_of_questions)

index = random.shuffle(list_of_questions)

answers = []

for q in list_of_questions:
    print(q)
    answer = input("True or False? (Enter T/F): ")
    if answer == "T" or answer == "t": 
        answers.append(q)
    
print(answers)

# sample animal has key of number of "True"s and value of list of which QIDs are true for it

class Animal:
    def __init__(self, name, num_true, qid_list) -> None:
        self.name = name
        self.num_true = num_true
        self.qid_list = qid_list
    
    def get_name(self):
        return self.name


Animals = df.iloc[:,1]
print(Animals)

# sample_animals = 

# for animal_name in df:
#     Animal()
# sample_animals = [
#     Animal('bird', 4, ["Q1", "Q4", "Q6", "Q8"]),
#     Animal('goose', 4,["Q2", "Q4", "Q5", "Q9"]),
#     Animal('snake', 5, ["Q1", "Q3", "Q7", "Q8", "Q10"]),
#     Animal('moose', 4, ["Q1", "Q4", "Q9", "Q8"]),
#     Animal('cat', 7, ["Q2", "Q3", "Q5", "Q7", "Q9", "Q10", "Q1"]), 
#     Animal('dog', 5, ["Q1", "Q2", "Q5", "Q7", "Q10"]),
#     Animal('elephant', 10, ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]),
#     Animal('lion', 3, ["Q3", "Q6", "Q9"]),
#     Animal('tiger', 8, ["Q2", "Q4", "Q6", "Q8", "Q10", "Q3", "Q7", "Q9"]),
#     Animal('rabbit', 2, ["Q1", "Q5"]),
#     Animal('snake', 6, ["Q2", "Q4", "Q6", "Q8", "Q10", "Q9"]),
#     Animal('monkey', 9, ["Q1", "Q3", "Q8", "Q7", "Q9", "Q2", "Q10", "Q4", "Q6"]),
#     Animal('horse', 1, ["Q10"]),
#     Animal('penguin', 6, ["Q2", "Q4", "Q6", "Q8", "Q10", "Q7"]),
#     Animal('koala', 3, ["Q1", "Q3", "Q5"]),
#     Animal('dolphin', 8, ["Q1", "Q3", "Q5", "Q7", "Q9", "Q10", "Q8", "Q4"]),
#     Animal('shark', 5, ["Q2", "Q4", "Q6", "Q8", "Q10"]),
#     Animal('bear', 7, ["Q3", "Q6", "Q9", "Q1", "Q5", "Q8", "Q2"]),
#     Animal('frog', 2, ["Q2", "Q4"]),
#     Animal('cheetah', 9, ["Q1", "Q3", "Q5", "Q7", "Q9", "Q4", "Q10", "Q2", "Q6"]),
#     Animal('elephant', 4, ["Q2", "Q10", "Q6", "Q7"]),
#     Animal('giraffe', 10, ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]),
#     Animal('wolf', 1, ["Q1"])
# ]        








# # sample_animals = [sample_animal1, sample_animal2, sample_animal3]

# num_of_correct_qids = 0

# # this works for checking if certain question id is in answers list
# # for a in answers:
# #     if "Q2" in a: #where a is a tuple with the t/f and the QID
# #         print("in")
# #     else:
# #         print("not in")
        

# #makes a list of the animals that match the correct number of true answers
# #TODO: make this choose the CLOSEST animals, not just the exact match
# def tally_closeness_check (correct_num, sample_list):
#     new_list = []
#     for animal in sample_list:
#         if animal.num_true == correct_num:
#             new_list.append(animal)
#     return new_list
        

# #returns the amount of correct QIDs for a given sample
# def qid_closeness_check (sample, answers):
#     # potential_samples = []
#     # for sample in samples:
#     #     if sample.num_true == 4:
#     #         potential_samples.append(sample) #animal object is added only if it has the correct number of trues
    
#     num_correct = 0
    
#     for idx, item in enumerate(answers):
#         for qid in sample.qid_list:
#             if qid == item: 
#                 # print(f'{qid} is in answers at index {idx}')
#                 num_correct += 1
    
#     return num_correct
            
            

# #list of animals that match the number of correct true answers
# potential_animals = tally_closeness_check(len(answers), sample_animals)
# print("Possible animals: ", end=' ')
# [print(i.get_name(), end=', ') for i in potential_animals] # print animals that mactched the tally


# max_correct_qids = 0
# best_animal:Animal = None

# # the animal in the new list with the highest amount of correct QIDs is chosen
# for animal in potential_animals:
#     num_correct = qid_closeness_check(animal, answers)
    
#     if num_correct > max_correct_qids:
#         max_correct_qids = num_correct
#         best_animal = animal
  
# if best_animal is not None:  
#     print(f'\nThe best animal is {best_animal.get_name()}') 
# else:
#     print("\nno animal is good")
        


# # Other TODOS:
# #  - random tiebreaker if animals are still tied
# #  - make a guess no matter what
# #  - find closest match for first phase of matching, top 3 closest maybe?


# ####### Overall Process Idea ########## 
# # get all answers from first part of each tuple in answers list, and choose animal based on total and which has the most number of the same (true) question IDs

# # Ideas: 
# #   - way to check database/file (however we're storing info, probably db), and edit animal entries, especially ones made by users
# #       - for ex: new animal "beaver" created based on users answers to questions, but as admin you think it necessary to change some answers associated with beaver to be more accurate
# #       - sort tuples in list by QID's?
# #  