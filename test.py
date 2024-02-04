import random

list_of_questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]

index = random.shuffle(list_of_questions)

answers = []

for q in list_of_questions:
    print(q)
    answer = input("True or False? (Enter T/F): ")
    if answer == "T" or answer == "t": 
        answers.append((answer, q))
    
print(answers)

sample_animal = ["Q1", "Q4", "Q6"]
num_of_correct_qids = 0

# this works for checking if certain question id is in answers list
# for a in answers:
#     if "Q2" in a: #where a is a tuple with the t/f and the QID
#         print("in")
#     else:
#         print("not in")
        
# not efficient, but can use this method to check and count how many correct QIDs are in the answers list, which can be used to further compare animals
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