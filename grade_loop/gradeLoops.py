# gradeLoops.py

# Assignment: Calculate the letter grade for the average of 5
# numerical scores. Must use loops.

loop = 5
score_inputs = []
print()
print()

def grade(score):
    if score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 63:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"
    
while loop > 0:
    user_input = int(input("Please enter a numeric score between 0 and 100: "))
    if user_input < 0 or user_input > 100: # Test for valid entries
        print("Invalid entry. Please try again.")
        user_input = 0
    else:
        score_inputs.append(user_input)
        loop -= 1 

final_score = sum(score_inputs) / 5
grade_letter = grade(final_score)

print(f"For an average score of {final_score}, your grade is {grade_letter}.")

print()
print()