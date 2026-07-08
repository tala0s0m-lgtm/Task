from folder1.sum import summation
from folder1.sub import calculate_Subtraction
from folder2.avr import average
from folder2.max import maximum

choice = int(input("Choose operation:\n1 - Add\n2 - Sub\n3 - max\n4 - Avg\n> "))

match choice:
    case 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = summation(num1, num2)
        print(f"The sum is: {result}")

    case 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        result = calculate_Subtraction(num1, num2) 
        print(f"The difference is: {result}")

    case 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = maximum(num1, num2)
        print(f"The maximum is: {result}")

    case 4:
        list_of_numbers = input("Enter numbers separated by spaces: ")
        
        
        cleaned_list = [int(num) for num in list_of_numbers.split()]
        
        result = average(cleaned_list)
        print(f"The average is: {result}")

    case _:
        print("Invalid choice.")