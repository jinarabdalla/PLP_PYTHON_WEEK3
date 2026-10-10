# grade_reporter.py

scores = [72, 45, 90, 61, 38]

total_score = 0
pass_count = 0
fail_count = 0
num_students = len(scores)

print("==============================")
print("       CLASS GRADE REPORT     ")
print("==============================")

for score in scores:
    # Add to running total
    total_score += score
    
    # Determine letter grade using if / elif / else
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    print(f"Score: {score} -> Grade: {grade}")
    
    # Count passes (50 or more) and fails (below 50)
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

# Calculate average rounded to one decimal place
if num_students > 0:
    average = total_score / num_students
    rounded_average = round(average, 1)
else:
    rounded_average = 0.0

print("------------------------------")
print(f"Passed Learners: {pass_count}")
print(f"Failed Learners: {fail_count}")
print(f"Class Average: {rounded_average}")
print("==============================")
