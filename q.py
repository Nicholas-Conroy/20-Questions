import pandas as pd

df = pd.read_csv("zoo2.csv")


# initiate array of animal objects
sample_animals = []

class HotAnimal:
    def __init__(self, name, id_list) -> None:
        self.name = name
        self.id_list = id_list

    def get_name(self):
        return self.name
    def get_id(self):
        return self.id_list

# pulling animals from df
for animal_name, row in df.iterrows():
    animal_id = row[1:]  # Slice from the second column to the last column
    animal_id_list = list(animal_id)

    name = row[0]

    sample_animals.append(HotAnimal(name, animal_id_list))
    
for i in sample_animals:
    print(i.get_name())