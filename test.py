import random

list_of_questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]

index = random.shuffle(list_of_questions)

answers = []

for q in list_of_questions:
    print(q)
    answer = input("True or False? (Enter T/F): ")
    if answer == "T" or answer == "t": 
        answers.append((answer, q))
    
print(answers)

# sample animal has key of number of "True"s and value of list of which QIDs are true for it
sample_animal1 = {4: ["Q1", "Q4", "Q6", "Q8"]}
sample_animal2 = {4: ["Q2", "Q4", "Q5", "Q9"]}
sample_animal3 = {4: ["Q3", "Q7", "Q8", "Q10"]}

samples = [sample_animal1, sample_animal2, sample_animal3]

num_of_correct_qids = 0

# this works for checking if certain question id is in answers list
# for a in answers:
#     if "Q2" in a: #where a is a tuple with the t/f and the QID
#         print("in")
#     else:
#         print("not in")
        
# not efficient, but can use this method to check and count how many correct QIDs are in the answers list, which can be used to further compare animals

# def closest_animal (samples, answers):
#     potential_samples = []
#     for sample in samples:
#         if sample
#             potential_samples.
        
for idx, item in enumerate(answers):
    for qid in sample_animal:
        if qid in item: #where a is a tuple with the t/f and the QID
            print(f'{qid} is in answers at index {idx}')
            num_of_correct_qids += 1
            
print("Num of correct QIDS: " + str(num_of_correct_qids))





####### Overall Process Idea ########## 
# get all answers from first part of each tuple in answers list, and choose animal based on total and which has the most number of the same (true) question IDs

# Ideas: 
#   - way to check database/file (however we're storing info, probably db), and edit animal entries, especially ones made by users
#       - for ex: new animal "beaver" created based on users answers to questions, but as admin you think it necessary to change some answers associated with beaver to be more accurate
#       - sort tuples in list by QID's?
#  