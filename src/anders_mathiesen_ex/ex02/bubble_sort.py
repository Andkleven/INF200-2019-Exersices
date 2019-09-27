def sort_list(list_data):
    new_data = list(list_data)
    for number in range(len(list_data)):
        if number == len(list_data) - 1:
            break
        first_number = new_data[number]
        second_number = new_data[number + 1]
        if first_number > second_number:
            new_data[number] = second_number
            new_data[number + 1] = first_number
    return new_data


def bubble_sort(random_list):
    for _ in range(len(random_list)):
        random_list = sort_list(random_list)
    return tuple(random_list)


if __name__ == "__main__":
    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
