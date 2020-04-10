#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # insert weights into a hashtable
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)
    
    # find both indices that add up to limit
    for index, weight in enumerate(weights):
        deficit = limit - weight
        index2 = hash_table_retrieve(ht, deficit)
        
        if index2:
            return index2, index

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
