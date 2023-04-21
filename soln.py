list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {"id": "3", "marks": 90, "roll_no": 11, "extra_info": {"hello": "world",}}
]
  
def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    count_dict = {}
    list_3 = list_1
    for i, data in enumerate(list_1):
        if data["id"] not in count_dict:
            count_dict[data["id"]] = []
        count_dict[data["id"]].append(i)

    
    for i, data in enumerate(list_2):
        if data["id"] not in count_dict:
            list_3.append(list_3[count_dict[list_2[i]["id"]]])
        else:
            idx = count_dict[data["id"]][0]
            print(list_3[idx])
            list_3[idx].update(data)

    # print(list_3)
    return list_3


list_3 = merge_lists(list_1, list_2)
