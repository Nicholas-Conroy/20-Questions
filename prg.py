import pandas as pd
from difflib import SequenceMatcher
import random
# import warnings
# warnings.simplefilter(action='ignore', category=FutureWarning)
from csv import writer

def append_to_csv(animal, id_list, df):
    # Check if animal is duplicate
    if check_animal_in_list(animal, df):
        return False
    List = id_list
    # adds animal name into the list ID at position 0
    List.insert(0, animal)
    # Opens csv in append mode. use w for write mode.
    with open("zoo2.csv",'a', newline='') as csvfile:
        # create CSV writer object, writes, and closes.
        writer_object = writer(csvfile)
        writer_object.writerow(List)
        csvfile.close()
    return True
# Documentation:
# https://docs.python.org/3/library/csv.html#module-csv


def check_animal_in_list(animal, df):
    animal_names = []
    for animal_name, row in df.iterrows():
        animal_names.append(row[0])

    if animal in animal_names:
        return True
    

def read_csv(csv):
    return pd.read_csv(csv)    
    

def return_questions(df):
    columns = list(df.columns[1:])
    return columns

# class that defines an "animal", each animal object has a name and an id (answers) list
class HotAnimal:
    def __init__(self, name, id_list) -> None:
        self.name = name
        self.id_list = id_list

    # getter methods
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
    # best_match_id = None

    for animal in sample_animals:
        comparison_result = similarity(animal.get_id(), answer)
        if comparison_result > best_match:
            best_match = comparison_result
            best_match_animal_name = animal.get_name()
            # best_match_id = animal.get_id()
            best_match_id = animal.get_id()
        if comparison_result == best_match:
            rand_choice = random.choice([0,1])
            # choose randomly from ties (not perfectly random rn, last option has best chance)
            if rand_choice == 0:
                best_match = comparison_result
                best_match_animal_name = animal.get_name()
            
        # TODO if comparison result equal to best match, randomly choose current or previous, and keep going
            
    # for displaying numbers
    # print(str(best_match_id) + "    ID")
    # print('percent closeness: ' + str(best_match))
    return best_match_animal_name