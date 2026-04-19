
    total = a - b
    return total         

answer = subtract(7, 3)
print("7 - 3 =", answer)

# TASK 2
# Define a function called "circle_area" that takes the
# RADIUS of a circle and RETURNS its area.
#
# Formula:  area = 3.14159 * radius * radius
#
# Test it with radii: 1, 5, 10
# Print each area rounded to 2 decimal places.
# Hint: round(number, 2)  rounds to 2 decimal places
# ------------------------------------------------------------

# 👉 Write your function here:


# 👉 Call it three times and print the areas:

def max_of_three(a,b,c):
  max = a 
  if (b>a and b>c):
    max=b
  elif(c>a and c>b):
    max = c
  else:
    max = a
  return max
  
print(max_of_three(4,6,17))


