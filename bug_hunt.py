# bug_hunt.py

count = 1
total = 0

# BUG: The condition was 'count < 5' instead of 'count <= 5', which caused a silent logic error stopping short of 5 (summing to 10 instead of 15). Fixed by changing it to '<= 5'.
# BUG: The while statement was missing a required colon at the end, causing a SyntaxError. Fixed by adding ':'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Attempting to concatenate a string and an integer directly causes a TypeError. Fixed by converting total to a string using str().
print("Sum of 1 to 5 is: " + str(total))
