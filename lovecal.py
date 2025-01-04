def calculate_love_score(name1, name2):
    # Combine the names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Calculate the score based on the frequency of each letter
    score = 0
    for char in combined_names:
        score += ord(char) - 96  # 'a' is 97 in ASCII, so subtract 96 to get 1 for 'a'
    
    # Normalize the score to a percentage
    score = score % 101  # Ensures the score is between 0 and 100
    return score

# Get names from user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate and display the love score
love_score = calculate_love_score(name1, name2)
print(f"The love score between {name1} and {name2} is: {love_score}%")
