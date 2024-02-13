
#uhhhh


my_list = [3,5,7,8,2,3,5,1,6,8, 9, 4, 7, 6, 4, 2, 1, 3, 8, 6, 10]

target_num = int(input("Enter a num: "))

closest_dist = abs(my_list[0] - target_num)

new_list = [None]*3 #list of 3 items
i = 0
for index, x in enumerate(my_list):
    cur_dist = abs(x - target_num)
    
    if cur_dist <= closest_dist:
        closest_dist = cur_dist
        print(index)
        new_list[i] = x
        i += 1
        if i == 3: i = 0
        
print(new_list)