if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

# Function to get user input for test scores
def get_test_scores(num_scores):
    scores = []
    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score {i+1}: "))
                if 0 <= score <= 100:  # Ensures valid score range
                    scores.append(score)
                    break
                else:
                    print("Please enter a score between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return scores

# Main program
def main():
    num_scores = 5
    print("Welcome to the Grade Calculator!")
    scores = get_test_scores(num_scores)
    
    # Calculate average and determine grade
    average = calculate_average(scores)
    grade = determine_grade(average)
    
    print(f"\nThe average score is: {average:.2f}")
    print(f"The corresponding letter grade is: {grade}")

# Run the program
if __name__ == "__main__":
    main()
