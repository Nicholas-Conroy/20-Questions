import pandas as pd
from difflib import SequenceMatcher
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
from csv import writer

# Might not work if csv file isint saved after being written to
def append_to_csv(animal, id_list):
    # Takes in new animal ID
    List = id_list
    # adds animal name into the list ID at position 0
    List.insert(0, animal)
    # Opens csv in append mode. use w for write mode.
    with open("zoo2.csv",'a', newline='') as csvfile:
        # create CSV writer object
        writer_object = writer(csvfile)
        # writes to the csv
        writer_object.writerow(List)
        # closes the object
        csvfile.close()
# Documentation:
# https://docs.python.org/3/library/csv.html#module-csv


def read_csv(csv):
    return pd.read_csv(csv)    
    

def return_questions(df):
    columns = list(df.columns[1:])
    return columns

class HotAnimal:
    def __init__(self, name, id_list) -> None:
        self.name = name
        self.id_list = id_list

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id_list

# pulling animals from df
def get_animals_list(df):
    
    sample_animals = []
    for animal_name, row in df.iterrows():
        animal_id = row[1:]  # Slice from the second column to the last column
        animal_id_list = list(animal_id)

        name = row[0]

        sample_animals.append(HotAnimal(name, animal_id_list))
    return sample_animals



# similarity checker
def similarity (a, b):
    # When None is passed, it uses the default comparison function
    return SequenceMatcher(None, a, b).ratio()
# Documentation: 
# https://docs.python.org/3/library/difflib.html#difflib.SequenceMatcher

def find_animal (sample_animals, answer):
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
    # print(str(best_match_id) + "    ID")
    # print('percent closeness: ' + str(best_match))
    return best_match_animal_name

# import random
# #uhhhh


# my_list = [3,5,7,8,2,3,5,1,6,8, 9, 4, 7, 6, 4, 2, 1, 3, 8, 6, 10]

# for i in range(0,10):
#     target_num = int(input("Enter a num: "))

#     closest_dist = abs(my_list[0] - target_num)

#     new_list = []
#     i = 0
#     for index, x in enumerate(my_list):
#         cur_dist = abs(x - target_num)
        
#         if cur_dist <= closest_dist:
#             closest_dist = cur_dist
#             print(index)
#             new_list.append(x)

#     print(new_list)
    
#     if len(new_list) > 3:     
#         for x in range(0, len(new_list)-3):
#             index_to_remove = random.randint(0,len(new_list)-1)
#             print("removing index: ", index_to_remove, ", which is the number ", new_list[index_to_remove])
#             del new_list[index_to_remove]
        
#     print(new_list)