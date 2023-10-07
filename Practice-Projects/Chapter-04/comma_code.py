def comma_code(list_value):
    string = ""

    # Empty list
    if len(list_value) == 0:
        return "The list is empty."

    # One item in list
    elif len(list_value) == 1:
        return list_value[0] + "."

    # Two items in list
    elif len(list_value) == 2:
        return list_value[0] + " and " + list_value[-1]

    # More than two items in list
    elif len(list_value) > 2:
        for i in range(len(list_value) - 1):
            string = string + list_value[i] + ", "
        string = string + "and " + list_value[-1] + "."

    return string


spam = ["dog", "cat", "bat", "rat"]
print(comma_code(spam))
