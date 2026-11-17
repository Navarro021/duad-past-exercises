
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(my_list) > 1:
    first_item = my_list[0]
    last_index = len(my_list) - 1

    my_list[0] = my_list[last_index]
    my_list[last_index] = first_item

print(my_list)
