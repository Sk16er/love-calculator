

def love_calculator(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()

    combined_names = name1 + name2

    score = 0

    for char in combined_names:
        score += ord(char) 

    love_percentage = score % 101  
    return love_percentage

# Get names from the user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate the love percentage
percentage = love_calculator(name1, name2)


print(f"The love compatibility between {name1} and {name2} is {percentage}%")
