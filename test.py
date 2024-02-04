import random
import numpy

list_of_questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]

index = random.shuffle(list_of_questions)

answers = []

for q in list_of_questions:
    print(q)
    answer = input("True or False? (Enter T/F): ")
    answers.append((answer, q))
    
print(answers[0][0])

# this works for checking if certain question id is in answers list
for a in answers:
    if "Q2" in a: #where a is a tuple with the t/f and the QID
        print("in")
    else:
        print("not in")
        
        
# get all answers from first part of each tuple in answers list, and choose animal based on total and which has the most number of the same (true) question IDs


# Ideas: 
#   - way to check database/file (however we're storing info, probably db), and edit animal entries, especially ones made by users
#       - for ex: new animal "beaver" created based on users answers to questions, but as admin you think it necessary to change some answers associated with beaver to be more accurate
# 