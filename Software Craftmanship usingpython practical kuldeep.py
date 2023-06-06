def find_common_and_unique_elements(list1, list2):
    common_elements = []
    unique_elements = []

    # Iterate over the elements in the first list
    for element in list1:
        if element in list2:
            # Common element found, add it to the common_elements list
            common_elements.append(element)
        else:
            # Unique element found in list1, add it to the unique_elements list
            unique_elements.append(element)

    # Iterate over the elements in the second list
    for element in list2:
        if element not in list1:
            # Unique element found in list2, add it to the unique_elements list
            unique_elements.append(element)

    return common_elements, unique_elements


# Test Case  : 
list1 = [10, 20, 30, 40, 50, 70]
list2 = [40, 50, 60, 70, 80, 90]
common, unique = find_common_and_unique_elements(list1, list2)

print("Common elements:", common)
print("Unique elements:", unique)