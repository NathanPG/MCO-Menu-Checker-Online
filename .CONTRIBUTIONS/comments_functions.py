# add comment into dictionary

#assume meal is always in dict_data
def add_comment_into_dictionary(comment, meal, dict_data):
    comment_ = str(comment)
    if meal not in dict_data:
        raise Exception("meal not in dict_data")
    
    dict_data[meal].append(comment_)
    
#create dictionary with given list(list of string)
def create_dict(key_list):
    result = {}
    if len(key_list) == 0:
        raise Exception("input list is empty")
    
    for i in key_list:
        result[i] = []
        
    return result
    
def delete_element_in_dictionary(comment, meal, dict_data):
    comment_ = str(comment)
    if meal not in dict_data:
        raise Exception("meal not in dict_data")
    
    for i in dict_data[meal]:
        if i == comment_:
            dict_data[meal].remove(i)
            return True
        
    return False
    
def clear_dictionary(dict_data):
    dict_data.clear()
    
    
    
    
if __name__ == "__main__":
    data = ["apple", "pizza", "omelet"]
    dict_data = create_dict(data)
    #print(dict_data)
    
    dict_data = {"omelet": []}
    meal = "omelet"
    comment = "omelet is great"
    add_comment_into_dictionary(comment, meal, dict_data)
    #print(dict_data["omelet"])
    
    result = delete_element_in_dictionary(comment, meal, dict_data)
    #print(result)
    
    clear_dictionary(dict_data)
    #print(dict_data)



