import random
#uhhhh


my_list = [3,5,7,8,2,3,5,1,6,8, 9, 4, 7, 6, 4, 2, 1, 3, 8, 6, 10]

for i in range(0,10):
    target_num = int(input("Enter a num: "))

    closest_dist = abs(my_list[0] - target_num)

    new_list = []
    i = 0
    for index, x in enumerate(my_list):
        cur_dist = abs(x - target_num)
        
        if cur_dist <= closest_dist:
            closest_dist = cur_dist
            print(index)
            new_list.append(x)

    print(new_list)
    
    if len(new_list) > 3:     
        for x in range(0, len(new_list)-3):
            index_to_remove = random.randint(0,len(new_list)-1)
            print("removing index: ", index_to_remove, ", which is the number ", new_list[index_to_remove])
            del new_list[index_to_remove]
        
    print(new_list)