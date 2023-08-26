# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆


# #Write your code below this row 👇


# #Setup elements count
# Number_of_elements = 0
# total_weight = 0

# #count how many elements are in each set
# for height in student_heights:
#   Number_of_elements += 1

# #add all elements together
# for height in student_heights:
#   total_weight += int(height)

# #Do math

# after_round_averaged_weight = round(total_weight / Number_of_elements)

# print(after_round_averaged_weight)
total = 0
for number in range(1,101):
    total += number
print(total)