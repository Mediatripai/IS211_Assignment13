print("Want to Play a Game?")
def fibonacci(n):
    """
    Recursively computes the nth Fibonacci number.
    :param n: Index of the Fibonacci sequence (non-negative integer)
    :return: The nth Fibonacci number
    """
    # Base case: if n is 0, return 0 (the first number in the Fibonacci sequence)
    if n <= 0:
        return 0
    
    # Base case: if n is 1, return 1 (the second number in the Fibonacci sequence)
    elif n == 1:
        return 1
    
    # Recursive case: Return the sum of the two preceding Fibonacci numbers
    # This represents the recurrence relation F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    """
    Recursively computes the greatest common divisor (GCD) of two integers.
    :param a: First integer
    :param b: Second integer
    :return: GCD of a and b
    """
    # Base case: If b is 0, the GCD is a
    # This follows from the property that GCD(a, 0) = a
    if b == 0:
        return a
    
    # Recursive case: Replace (a, b) with (b, a % b) and call gcd again
    # This is based on Euclid's algorithm: GCD(a, b) = GCD(b, a % b)
    else:
        return gcd(b, a % b)

def compareTo(s1, s2):
    """
    Recursively compares two strings lexicographically.
    :param s1: First string
    :param s2: Second string
    :return: Negative if s1 < s2, zero if s1 == s2, positive if s1 > s2
    """
    # Base case: If both strings are empty, they are equal
    if not s1 and not s2:
        return 0
    
    # Base case: If s1 is empty but s2 is not, s1 is smaller
    elif not s1:
        return -ord(s2[0])  # Negative ASCII value of the first character in s2
    
    # Base case: If s2 is empty but s1 is not, s1 is larger
    elif not s2:
        return ord(s1[0])  # Positive ASCII value of the first character in s1
    
    # Base case: If the first characters of s1 and s2 are not equal, compare them
    elif s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])  # Difference in ASCII values of the first characters
    
    # Recursive case: Compare the rest of the strings (excluding the first character)
    else:
        return compareTo(s1[1:], s2[1:])

# Main function to interact with the user
def main():
    while True:
        # Display the menu options
        print("\nChoose an option:")
        print("1. Calculate nth Fibonacci number")
        print("2. Find GCD of two numbers")
        print("3. Compare two strings")
        print("4. Exit")
        
        # Prompt the user for their choice
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # Option 1: Calculate Fibonacci number
            try:
                n = int(input("Enter a non-negative integer n: "))
                if n < 0:
                    print("Please enter a non-negative integer!")  # Validation for negative input
                else:
                    # Call the fibonacci function and display the result
                    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
            except ValueError:
                print("Invalid input. Please enter an integer.")  # Handle invalid input
        
        elif choice == "2":
            # Option 2: Find GCD of two numbers
            try:
                # Get two integers from the user
                a = int(input("Enter the first number (a): "))
                b = int(input("Enter the second number (b): "))
                
                # Call the gcd function and display the result
                print(f"The GCD of {a} and {b} is: {gcd(a, b)}")
            except ValueError:
                print("Invalid input. Please enter integers.")  # Handle invalid input
        
        elif choice == "3":
            # Option 3: Compare two strings
            # Get two strings from the user
            s1 = input("Enter the first string (s1): ")
            s2 = input("Enter the second string (s2): ")
            
            # Call the compareTo function to compare the strings
            result = compareTo(s1, s2)
            if result < 0:
                print(f'"{s1}" is less than "{s2}".')
            elif result == 0:
                print(f'"{s1}" is equal to "{s2}".')
            else:
                print(f'"{s1}" is greater than "{s2}".')
        
        elif choice == "4":
            # Option 4: Exit the program
            print("Goodbye!")
            break  # Exit the while loop
        
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please select a valid option.")

# Entry point of the program
if __name__ == "__main__":
    main()