"""
The program will:
- Take input for 3 numeric exam grades.
- Calculate and return the average test score.
- Determine the corresponding letter grade based on the grading scale.
- Display a message stating whether the student is passing or failing.


Grading Scale:
90+   → A (Passing)
80-89 → B (Passing)
70-79 → C (Passing)
60-69 → D (Passing)
0-59  → F (Failing)

Example 1:
Exams: 89, 90, 90
Average: 90
Grade: A
Student is passing.

Example 2:
Exams: 50, 51, 0
Average: 33
Grade: F
Student is failing.


Corrections made:
1. Ensured proper input conversion to integers.
2. Fixed incorrect variable name `exam_3` -> `exam_three`.
3. Fixed list syntax `[exam_one, exam_two, exam_three]`.
4. Removed unnecessary loop for sum calculation, used `sum(grades)`.
5. Fixed variable name typo `grdes` -> `grades`.
6. Corrected missing colon in `elif avg >= 80 and avg < 90:`.
7. Fixed mismatched quotation mark in `letter_grade = "C'`.
8. Added a condition to the last `elif`, replacing `elif:` with `else:`.
9. Fixed incorrect comparison `if letter-grade is "F":` to `if letter_grade == "F":`.
10. Corrected `print "Student is failing."` to `print("Student is failing.")`.
11. Rounded the average to 2 decimal places for better readability.

"""

# I added this function to ensure only valid integers are entered for exam grades
# Reason: Prevents program crashes when users input letters or invalid values
def get_grade(prompt):
    while True:
        try:
            grade = int(input(prompt))  # Try converting input to integer
          """
          'input()' function used for exam grades from the user.
          and input() returns a string then convert it to an integer using 'int()'
          then mathematical calculations can work.
          """
            return grade
        except ValueError:
            print("Invalid input. Only numbers are allowed.")  # Clear user message

# I fixed original input inconsistencies and used the safe input function instead of raw input()
exam_one = get_grade("Input exam grade one: ")         
exam_two = get_grade("Input exam grade two: ")         
exam_three = get_grade("Input exam grade three: ")     

# Tsion fixed the variable name inconsistency (was: exam_3, grades list had syntax errors)
grades = [exam_one, exam_two, exam_three]  

# Tsion added this: Corrected logic for summing the grades
# Reason: original loop was using 'grade' instead of 'grades' and overwrote the 'sum' function
total = 0
for grade in grades:
    total += grade # Simplified and corrected the accumulation logic

# Tsion fixed typo: 'grdes' to 'grades' and renamed 'sum' to 'total' to avoid conflict with built-in
avg = total / len(grades)

# Tsion fixed logic and syntax in conditional blocks (missing colons, invalid string quotes, wrong operators)
# Determining the letter grade

"""
'if', 'elif', 'else') used to check which range the 
average score falls into and assigns the appropriate grade.
"""

if avg >= 90:
    letter_grade = "A" # No change needed
elif avg >= 80:
    letter_grade = "B"  # Tsion simplified condition: 'avg < 90' is not needed due to elif
elif avg > 69:
    letter_grade = "C"  # Tsion fixed quote error ('C' -> "C")
elif avg >= 65:
    letter_grade = "D" # Tsion changed condition from 'avg <= 69 and avg >= 65' to just 'avg >= 65'
else:
    letter_grade = "F"  # Tsion fixed: added proper else block with condition fallback

# Printing results

"""
'for' loop is used to iterate over the 'grades' list 
and print each exam score separately.
"""

# Tsion fixed the for-loop indentation and printing logic
# Reason: The original printed average and grade inside the loop by mistake
for grade in grades:
    print("Exam:", grade)  # Tsion changed from string concatenation to comma

# Tsion moved average and grade printing outside the loop
print("Average:", avg)
print("Grade:", letter_grade)

# Tsion fixed: original used 'letter-grade is "F"' (invalid syntax)
# Changed to proper variable name and used '==' for comparison
if letter_grade == "F":
    print("Student is failing.") # Tsion added parentheses 
else:
    print("Student is passing.") # Tsion added parentheses 
