# max_function

def maximum(a, b):
    """
    Function to find the maximum of two numbers
    """
    if a > b:
        return a
    else:
        return b


def find_max(numbers):
    """
    Function to find the maximum number in a list
    (Extra function, not used in main)
    """
    if not numbers:  
        return None
    
    max_value = numbers[0]
    
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value