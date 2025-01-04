def calculate_love_score(name1, name2):
    """
    Calculate the love score between two names based on a simple algorithm.
    """
    combined_names = (name1 + name2).lower()
    score = sum(ord(char) for char in combined_names if char.isalpha()) % 101 # Love score between 0 and 100
    return score

def main():
    """
    Main function to run the love calculator.
    """
    print("Welcome to the Love Calculator!")
    
    # Get user input
    name1 = input("Enter the first name: ").strip()
    name2 = input("Enter the second name: ").strip()
    
    # Validate input
    if not name1.isalpha() or not name2.isalpha():
        print("Please enter valid names containing only alphabetic characters.")
        return
    
    # Calculate love score
    score = calculate_love_score(name1, name2)
    
    # Display the result
    print(f"The love score for {name1} and {name2} is: {score}%")

if __name__ == "__main__":
    main()
