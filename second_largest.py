#write a program to find the second largest number in an array
def second_largest(arr):
    unique_element=list(set(arr))
    if len(unique_element)<2:
        return "No second largest element"
    
    unique_element.sort()
    return unique_element[-2]

arr=[10,20,4,45,99,24]
print("Second largest: ",second_largest(arr))