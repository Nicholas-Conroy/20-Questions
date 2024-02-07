import random

list_of_questions = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8", "Q9", "Q10"]

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
    def __init__(self, num_true, qid_list) -> None:
        self.num_true = num_true
        self.qid_list = qid_list

sample_animal1 = Animal(4, ["Q1", "Q4", "Q6", "Q8"])
sample_animal2 = Animal(4,["Q2", "Q4", "Q5", "Q9"])
sample_animal3 = Animal(5, ["Q1", "Q3", "Q7", "Q8", "Q10"])

sample_animals = [sample_animal1, sample_animal2, sample_animal3]

num_of_correct_qids = 0

# this works for checking if certain question id is in answers list
# for a in answers:
#     if "Q2" in a: #where a is a tuple with the t/f and the QID
#         print("in")
#     else:
#         print("not in")
        
# not efficient, but can use this method to check and count how many correct QIDs are in the answers list, which can be used to further compare animals

# for now, returns the amount of correct QIDs for a given sample
def closeness_check (sample, answers):
    # potential_samples = []
    # for sample in samples:
    #     if sample.num_true == 4:
    #         potential_samples.append(sample) #animal object is added only if it has the correct number of trues
    
    num_correct = 0
    
    for idx, item in enumerate(answers):
        for qid in sample.qid_list:
            if qid == item: 
                print(f'{qid} is in answers at index {idx}')
                num_correct += 1
    
    return num_correct
            
            
sample1_closeness = closeness_check(sample_animals[0], answers)   
sample2_closeness = closeness_check(sample_animals[1], answers)     
sample3_closeness = closeness_check(sample_animals[2], answers)     
  
       
print("Num of correct QIDS for Sample 1: " + str(sample1_closeness))
print("Num of correct QIDS for Sample 2: " + str(sample2_closeness))
print("Num of correct QIDS for Sample 3: " + str(sample3_closeness))






####### Overall Process Idea ########## 
# get all answers from first part of each tuple in answers list, and choose animal based on total and which has the most number of the same (true) question IDs

# Ideas: 
#   - way to check database/file (however we're storing info, probably db), and edit animal entries, especially ones made by users
#       - for ex: new animal "beaver" created based on users answers to questions, but as admin you think it necessary to change some answers associated with beaver to be more accurate
#       - sort tuples in list by QID's?
#  